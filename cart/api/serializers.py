

from rest_framework import serializers

from cart.models  import Cart



class CartSerializer(serializers.ModelSerializer):
    created_by = serializers.CurrentUserDefault()
    class Meta:
        model = Cart
        fields = "__all__"
        # [
        #     'created_by',
        #     'order_items',
        # ]

class removeOBJserializer(serializers.Serializer):
    ID_OF_Item = serializers.IntegerField


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