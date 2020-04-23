from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import (
                Cart
)

from books.models import Proposed_Book


from cart.api.serializers import (
                CartSerializer ,
                removeOBJserializer

)

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class Remove_Item_from_list(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = removeOBJserializer

    def delete(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        if (serializer.is_valid()):
            data = serializer.data
            Proposed_Book.objects.get(id=data['ID_OF_Item'])

            return Response(status=status.HTTP_200_OK)

        else:
            content = {'detail': 'Failed to delete item'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


            # def get_queryset(self):
    #     user = self.request.user
    #     queryset = self.queryset.filter(created_by='user')
    #     return queryset
    # def perform_create(self, serializer):
    #     serializer.save()
