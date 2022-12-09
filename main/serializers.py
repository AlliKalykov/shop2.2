from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Category, Brand, Clothes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_description')


class ClothesInCategorySerializer(serializers.ModelSerializer):
    clothes_brand = serializers.SlugRelatedField(read_only=True, slug_field='brand_name')
    class Meta:
        model = Clothes
        fields = ('id', 'clothes_name', 'clothes_slug', 'clothes_price', 'clothes_image', 'clothes_brand',)


class CategoryDetailSerializer(serializers.ModelSerializer):
    clothes = ClothesInCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_slug', 'category_description', 'clothes')


class ClothesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ('id', 'clothes_name', 'clothes_description', 'clothes_slug', 'clothes_type', 'clothes_season', 'clothes_price', 'clothes_image', 'clothes_brand', 'clothes_category',)