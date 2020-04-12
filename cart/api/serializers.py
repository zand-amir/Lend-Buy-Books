

from rest_framework import serializers

from cart.models  import ( Cart,
                           Order
                           )

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ( 'url', 'items',)

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ( 'url', 'items','cart')