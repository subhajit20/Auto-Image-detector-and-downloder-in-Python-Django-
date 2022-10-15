from rest_framework import serializers
import re

class LinkSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=400)
    
    def validate_link(self, value):
        if re.search('^http://|^https://',value) is None:
            raise serializers.ValidationError("Image link is not valid")
        else:
            return value