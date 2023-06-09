from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('book.urls')),
    path('profile/', include('user_profile.urls')),
    path('api/', include('api.urls')),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
