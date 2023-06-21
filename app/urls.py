from django.urls import path

from app.views import ViewList


urlpatterns = [
    path('', ViewList.as_view(), name='view'),

]