from rest_framework import serializers

from .models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    # реализуйте сериализацию объектов модели Book
    class Meta:
        model = Book
        fields = '__all__'

    #доп задание
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['orders_count'] = Order.objects.filter(books=instance.id).count()
        return representation


class OrderSerializer(serializers.ModelSerializer):
    # добавьте поля модели Order
    class Meta:
        model = Order
        fields = '__all__'

    #доп задание
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['books'] = Book.objects.filter(id__in=instance.books.all()).values()
        return representation
