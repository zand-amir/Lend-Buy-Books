

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


# class ProductsSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#         model = Products
#         fields = '__all__'
#
#
#
# class OrdersSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Orders
#         fields = '__all__'