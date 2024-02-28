from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'category', 'price', 'quantity', 'barcode')

class CategorySerializer(serializers.Serializer):
    category = serializers.CharField(max_length=255)

class SortedItemSerializer(ItemSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'category', 'price', 'quantity', 'barcode')
        ordering = ['-price']  # Order by price in descending order
