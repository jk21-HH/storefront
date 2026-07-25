from rest_framework import serializers
from decimal import Decimal

from store.models import Cart, CartItem, Product, Collection, Review

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection', 'collection_title']
    
    collection_title = serializers.CharField(source='collection.title', read_only=True)

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'date']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)

class BasicProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax']

class CartItemSerializer(serializers.ModelSerializer):
    product = BasicProductSerializer()
   
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

    total_price = serializers.SerializerMethodField(method_name='get_total_price')

    def get_total_price(self, cart_item: CartItem) -> float:
        return cart_item.quantity * cart_item.product.price_with_tax
    
class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']

    def get_total_price(self, cart: Cart) -> float:
        return sum([item.quantity * item.product.price_with_tax for item in cart.items.all()])

class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']


    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('No product with the given ID found')
        
        return value
    
    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        
        try: 
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)

        return self.instance


    