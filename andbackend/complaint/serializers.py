from rest_framework import serializers
from django.contrib.auth.models import User
from complaint.models import Category, Complaint, Image

# Sorun cozulmezse Silinecek
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'icon')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            username = attrs.get('username', instance.username)
        else:
            username = attrs["username"]
        return User.objects.get(username=username)

class ComplaintSerializer(serializers.ModelSerializer):
    reporter = serializers.SlugRelatedField(many=False, slug_field='username')
    category = serializers.SlugRelatedField(many=False, slug_field='name')

    class Meta:
        model = Complaint
        fields = ('id', 'address', 'city', 'longtitude', 'latitude', 'downvote',
                  'upvote', 'category', 'reporter', 'date', 'title')

    # def restore_object(self, attrs, instance=None):
    #     print 'Da fuck'
    #     print attrs
    #     attrs['reporter'] = UserSerializer(data=attrs['reporter']).object
    #     attrs['category'] = CategoryListSerializer(data=attrs['category']).object
    #     print attrs
    #     return Complaint(**attrs)

class ComplaintListSerializer(serializers.ModelSerializer):
    reporter = serializers.Field('reporter.username')
    category = CategoryListSerializer()

    class Meta:
        model = Complaint
        fields = ('id', 'title', 'reporter', 'category', 'date', 'city', 'upvote')


class ComplaintDetailSerializer(serializers.ModelSerializer):
    reporter = serializers.Field('reporter.username')
    category = serializers.Field('category.name')
    # images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Complaint
        fields = ('id', 'address', 'city', 'longtitude', 'latitude', 'downvote',
                  'upvote', 'category', 'reporter', 'date', 'title')


class ImageSerializer(serializers.ModelSerializer):
    complaint = serializers.Field('complaint.id')
    uploader = serializers.Field('uploader.username')

    class Meta:
        model = Image
        fields = ('id', 'complaint', 'uploader', 'image')
