from rest_framework import serializers
from .models import Book,Author
from django.utils import timezone
from datetime import datetime


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name','email']
# class BookSerializer(serializers.HyperlinkedModelSerializer):
#     days_since_created = serializers.SerializerMethodField()
#     author = AuthorSerializer()
    
#     class Meta:
#         model = Book
#         fields = ['url','id','title','content','publication_year','author','days_since_created']
    
#     def get_days_since_created(self,obj):
#         return (datetime.now().date() - obj.created_date.date()).days
#     def create(self,validated_data):
#         author_data = validated_data.pop('author')
#         author,created = Author.objects.get_or_create(email=author_data['email'],defaults=author_data)
#         book = Book.objects.create(author=author,**validated_data)
#         return book
#     def update(self, instance, validated_data):
#         author_data = validated_data.pop('author')
    
#         # Attempt to retrieve the existing author by email
#         try:
#             author = Author.objects.get(email=author_data['email'])
            
#             # Update the author's name if provided
#             if 'name' in author_data:
#                 author.name = author_data['name']
#                 author.save()
        
#         # If the author doesn't exist, create a new one
#         except Author.DoesNotExist:
#             author = Author.objects.create(**author_data)
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.publication_year = validated_data.get('publication_year', instance.publication_year)
#         instance.author = author
#         instance.save()
#         return instance

class BookSerializer(serializers.HyperlinkedModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    author_name = serializers.CharField(source='author.name')
    author_email = serializers.EmailField(source='author.email')

    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'content', 'publication_year', 'author_name', 'author_email', 'days_since_created']

    def get_days_since_created(self, obj):
        return (datetime.now().date() - obj.created_date.date()).days

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(email=author_data['email'], defaults={'name': author_data['name']})
        book = Book.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        
        # Retrieve the existing author by email
        author, created = Author.objects.get_or_create(email=author_data['email'])
        
        # Optionally update the author's name
        if 'name' in author_data:
            author.name = author_data['name']
            author.save()
        
        # Update the book instance
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.publication_year = validated_data.get('publication_year', instance.publication_year)
        instance.author = author
        instance.save()
        return instance
