from rest_framework import serializers
from .models import Post



class ViewCreateSerializer(serializers.ModelSerializer):


    # значение автора по умолчанию при создании пупликации
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    category_name = serializers.CharField(source="category.title",
                                          read_only=True
                                          )
    user_name = serializers.CharField(source="author.username",
                                          read_only=True
                                          )

    class Meta:
        fields = '__all__'
        model = Post


class OnlyReadalizer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Post