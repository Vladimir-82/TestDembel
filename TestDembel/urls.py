from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # подключение авторизации по сессии
    path('api/v1/', include('app.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
