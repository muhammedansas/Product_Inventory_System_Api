from rest_framework import serializers
from .models import Products, Variant, SubVariant
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone', 'is_active', 'is_admin', 'is_staff', 'created_at']


class SubVariantSerializer(serializers.ModelSerializer):
    variant = serializers.CharField(max_length=100)

    class Meta:
        model = SubVariant
        fields = ['id', 'subvariant_name','variant','stock']


class VariantSerializer(serializers.ModelSerializer):
    subvariants = SubVariantSerializer(many=True, read_only=True)
    product = serializers.CharField(max_length=100)

    class Meta:
        model = Variant
        fields = ['id', 'variant_name', 'subvariants', 'product']

    def validate(self, data):
        product = data.get('product')
        variant_name = data.get('variant_name')

        if Variant.objects.filter(variant_name=variant_name, product=product).exists():
            raise serializers.ValidationError("A variant with this name already exists for the specified product.")
        
        return data


class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True,read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'ProductID', 'ProductCode', 'ProductName', 'ProductImage', 'variants','CreatedUser']