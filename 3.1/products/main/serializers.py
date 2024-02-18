from rest_framework import serializers

from main.models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta:
        model = Review
        fields = '__all__'


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField()
    price = serializers.IntegerField()


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    comments = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'comments']
