from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Products,SubVariant,Variant
from authentication.models import User
from . serializer import ProductSerializer,UserSerializer,VariantSerializer,SubVariantSerializer

# Create your views here.


class ProductView(APIView):
    def get(self,request):
        try:
            user = User.objects.get(username=request.user)
        except User.DoesNotExist:
            return Response({"errors":"User not found"})    

        try:
            obj = Products.objects.prefetch_related('variants').all()
        except Products.DoesNotExist:
            return Response({"errors":"Products not found"}) 
        
        user_serializer = UserSerializer(user)
        product_serializer = ProductSerializer(obj,many=True)
        return Response({
            'user': user_serializer.data,
            'products': product_serializer.data
        }, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            Products.objects.create(
                ProductID = serializer.validated_data['ProductID'],
                ProductCode = serializer.validated_data['ProductCode'],
                ProductName = serializer.validated_data['ProductName'],
                ProductImage = serializer.validated_data['ProductImage'],
                CreatedUser = serializer.validated_data['CreatedUser']
            )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class VariantView(APIView):
    def get(self,request,product):
        print(product,"product")
        try:
            obj = Variant.objects.select_related('product').filter(product=product)
        except Variant.DoesNotExist:
            return Response({"errors":"Varient not found"})    
        serializer = VariantSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request):
        product_id = request.data['product']
        product_instance = Products.objects.get(id=product_id)
        serializer = VariantSerializer(data=request.data)
        if serializer.is_valid():
            Variant.objects.create(
                product = product_instance,
                variant_name = serializer.validated_data['variant_name']
            )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors,"eroor")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class SubVariantView(APIView):
    def get(self,request,product):
        try:
            obj = SubVariant.objects.select_related('variant').filter(variant__product=product)
        except SubVariant.DoesNotExist:
            return Response({"error":"Subvariant not found"})
        serializer = SubVariantSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def post(self,request):
        variant_id = request.data.get("variant")
        try:
            variant_instance = Variant.objects.get(id=variant_id)
        except Variant.DoesNotExist:
            return Response({"error": "Variant not found"}, status=404)
        
        serializer = SubVariantSerializer(data=request.data)
        if serializer.is_valid():
            SubVariant.objects.create(
            subvariant_name = serializer.validated_data['subvariant_name'],
            stock= serializer.validated_data['stock'],
            variant = variant_instance,
            )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AddStockView(APIView):
    def patch(self, request):
        subvariant_name = request.data.get('subvariant_name')
        incoming_stock = request.data.get('stock')
        
        if not subvariant_name or not incoming_stock:
            return Response({"error": "subvariant_name and stock are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            incoming_stock = int(incoming_stock)
            subvariant = SubVariant.objects.filter(subvariant_name=subvariant_name).first()
        except SubVariant.DoesNotExist:
            return Response({"error": "SubVariant with this name does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        subvariant.stock += incoming_stock
        subvariant.save()
            
        serializer = SubVariantSerializer(subvariant)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RemoveStockView(APIView):
    def patch(self, request):
        subvariant_name = request.data.get('subvariant_name')
        incoming_stock = request.data.get('stock')
        
        if not subvariant_name or not incoming_stock:
            return Response({"error": "subvariant_name and stock are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            incoming_stock = int(incoming_stock)
            subvariant = SubVariant.objects.filter(subvariant_name=subvariant_name).first()
        except SubVariant.DoesNotExist:
            return Response({"error": "SubVariant with this name does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        subvariant.stock -= incoming_stock
        subvariant.save()
            
        serializer = SubVariantSerializer(subvariant)
        return Response(serializer.data, status=status.HTTP_200_OK) 