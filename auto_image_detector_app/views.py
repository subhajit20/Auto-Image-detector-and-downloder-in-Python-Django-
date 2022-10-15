from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .lib.Scrap_Image import Search_Image,Download_Image
from .serializer import LinkSerializer


@api_view(['POST'])
def Search_The_Image(request):
    try:
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.data.get('link')
            flag = Search_Image(url)
            if flag:
                return Response({'imgurl':url},status=status.HTTP_200_OK)
            return Response({'error':'Image is not found'},status=status.HTTP_404_NOT_FOUND)
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'msg':"Something went wrong..."},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def Scrapp_Image(request):
    serializer = LinkSerializer(data=request.data)
    if serializer.is_valid():
        url = serializer.data.get('link')
        imgname = Download_Image(url)
        if imgname != False:
            return Response({'imagename':imgname,'flag':True},status=status.HTTP_200_OK)
        else:
            return Response({'msg':'No Images are there...','flag':False},status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error':serializer.errors,'flag':False},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetImage(request,imgname):
    file_path = f'pics/{imgname}.jpg'
    FilePointer = open(file_path,"rb")
    response = HttpResponse(FilePointer,content_type='application/jpg')
    response['Content-Disposition'] = 'attachment; filename={myimage}.jpg'.format(myimage=imgname)

    return response