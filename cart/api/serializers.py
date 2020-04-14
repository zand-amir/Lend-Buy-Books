

from rest_framework import serializers

from cart.models  import Cart


class CartSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.CurrentUserDefault()

    class Meta:
        model = Cart
        fields = [
            'created_by',
            'order_items',
        ]