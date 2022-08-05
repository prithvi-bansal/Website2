from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Website API')

# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Website API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.Website.com/policies/terms/",
#       contact=openapi.Contact(email="contact@website.local"),
#       license=openapi.License(name="Test License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('cache/', include('caching.urls')),
    path('thread/', include('thread.urls')),
    path('home/', include('users.urls')),
    path('post/', include('posts.urls')),
    path('pay/', include('payment.urls')),
    path('api/', include('api_url.api_urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view),
    path('accounts/', include('allauth.urls')),
    # path('oauth/', include('social_django.urls', namespace='social')),  # <-- here

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

