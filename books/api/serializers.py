from rest_framework import serializers
from ..models import Author, Category, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Author
        fields= ('name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields= ('name',)


class BookSerializer(serializers.ModelSerializer):

    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta: 
        model = Book
        fields= ('title', 'authors', 'published_date', 'categories', 
                 'average_rating', 'ratings_count', 'thumbnail')