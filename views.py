from rest_framework import status, viewsets, mixins, generics
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer, CategorySerializer, SortedItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request):
        # Check for duplicate barcode
        barcode = request.data.get('barcode')
        if Item.objects.filter(barcode=barcode).exists():
            return Response({'error': 'Item with barcode already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category = self.kwargs.get('category')
        if category:
            return Item.objects.filter(category=category)
        else:
            return Item.objects.none()  # Return empty list if category not provided

class SortedItemView(generics.ListAPIView):
    serializer_class = SortedItem


