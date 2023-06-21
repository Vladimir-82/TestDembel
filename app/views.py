from rest_framework import generics, permissions, viewsets

from app.models import Post
from app.serializers import ViewCreateSerializer
from app.permissions import IsAuthorOrReadOnly


class ViewCreateList(generics.ListCreateAPIView):
    '''Returns a list of posts for all users'''
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = ViewCreateSerializer




class UpdateDetailDelete(generics.RetrieveUpdateDestroyAPIView):
    '''Returns a list of posts for all users'''
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = ViewCreateSerializer





# меняем класс ViewSet и получаем нужный функционал
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ViewCreateSerializer


class ReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ViewCreateSerializer