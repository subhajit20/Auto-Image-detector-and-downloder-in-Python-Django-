from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from django.contrib import admin
from django.urls import path,include

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Auto image detector and downloder",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('auto_image_detector_app.urls')),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema")
]
