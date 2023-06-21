from rest_framework import serializers
from .models import Post


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'category', 'views')
        model = Post