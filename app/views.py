from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response

from app.models import Post, Category
from app.serializers import ViewCreateSerializer, Top3Readalizer
from app.permissions import IsAuthorOrReadOnly

import random



class MyResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ViewCreateList(generics.ListCreateAPIView):
    '''Returns a list of posts for all users'''
    # permission_classes = (permissions.IsAuthenticated,)
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
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = MyResultsSetPagination


    def get_object(self):
        '''
        Increases the number of views
        '''
        object = super().get_object()
        object.views += 1
        object.save()
        return object

    # один параметр
    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cat = Category.objects.get(pk=pk)
    #     return Response({'category': cat.title})

    # группа параметров
    @action(methods=['get'], detail=False)
    def categories(self, request):
        cats = Category.objects.all()
        return Response({'cats': [cat.title for cat in cats]})

    # группа параметров
    @action(methods=['get'], detail=False)
    def mails(self, request):
        mails = Post.objects.all()
        return Response({'mails': set(
            [post.author.email for post in mails if post.author.email])}
        )


class ViewTop3(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Top3Readalizer

    def get_queryset(self):
        queryset = Post.objects.all().order_by("-views")[:3]
        return queryset