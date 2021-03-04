from rest_framework import serializers
from ..models import Author, Comment, NewsPost


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class NewsPostSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return NewsPost.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.link = validated_data.get('link', instance.link)
        instance.creation_date = validated_data.get('creation_date', instance.creation_date)
        instance.amount_of_upvotes = validated_data.get('amount_of_upvotes',
                                                        instance.amount_of_upvotes)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.save()
        return instance

    class Meta:
        model = NewsPost
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
