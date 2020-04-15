from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import (
                Cart
)


from cart.api.serializers import (
                CartSerializer
)





class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = self.queryset.filter(created_by='user')
    #     return queryset
    # def perform_create(self, serializer):
    #     serializer.save()
