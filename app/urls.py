from django.urls import path, include

from app.views import ViewCreateList, UpdateDetailDelete, ReadOnlyViewSet
from rest_framework import routers


router = routers.DefaultRouter()
# меняем класс ViewSet и получаем нужный функционал
router.register(r'posts', ReadOnlyViewSet)


urlpatterns = [
    # path('posts', ViewCreateList.as_view(), name='view_create'),
    # path('posts/<int:pk>/', UpdateDetailDelete.as_view(), name='delete'),

    # path('posts', PostViewSet.as_view({'get': 'list'}), name='view'),
    # path('posts/<int:pk>/', PostViewSet.as_view({'put': 'update'}), name='update'),

    path('', include(router.urls))
]