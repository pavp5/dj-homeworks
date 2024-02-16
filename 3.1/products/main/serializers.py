from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    pass


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField()
    price = serializers.IntegerField()


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    pass
