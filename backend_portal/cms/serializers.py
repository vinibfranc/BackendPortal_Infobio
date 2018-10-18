from rest_framework import serializers

from .models import Category, Section, Content, Post, Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
