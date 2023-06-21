from rest_framework import generics, permissions

from app.models import Post
from app.serializers import ViewSerializer


class ViewList(generics.ListAPIView):
    '''Returns a list of posts for all users'''
    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = ViewSerializer
