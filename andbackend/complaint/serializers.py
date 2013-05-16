from rest_framework import serializers
from django.contrib.auth.models import User
from complaint.models import Category, Complaint

class ComplaintListSerializer(serializers.ModelSerializer):
    reporter = serializers.Field('reporter.username')
    category = serializers.Field('category.name')

    class Meta:
        model = Complaint
        fields = ('id', 'title', 'reporter', 'category', 'date', 'city', 'address')


class ComplaintDetailSerializer(serializers.ModelSerializer):
    reporter = serializers.Field('reporter.username')
    category = serializers.Field('category.name')
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Complaint
        fields = ('id', 'address', 'city', 'longtitude', 'latitude', 'downvote',
                  'upvote', 'images', 'category', 'reporter', 'date', 'title')

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'icon')
