from django.db import models
import uuid
from versatileimagefield.fields import VersatileImageField
from authentication.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Products(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    ProductID = models.BigIntegerField(unique=True)
    ProductCode = models.CharField(max_length=225,unique=True)
    ProductName = models.CharField(max_length=255)
    ProductImage = VersatileImageField(upload_to="uploads/", blank=True, null=True)  
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(blank=True, null=True)
    CreatedUser = models.ForeignKey(User, related_name="user%(class)s_objects", on_delete=models.CASCADE)
    IsFavourite = models.BooleanField(default=False)
    Active = models.BooleanField(default=True)
    HSNCode = models.CharField(max_length=255, blank=True, null=True)
    TotalStock = models.DecimalField(default=0.00, max_digits=20, decimal_places=8, blank=True, null=True)


    class Meta:
        db_table = "products_product"
        verbose_name = _("product")
        verbose_name_plural = _("products")
        unique_together = (("ProductCode", "ProductID"),)
        ordering = ("-CreatedDate", "ProductID")

    def __str__(self):
        return self.ProductName


class Variant(models.Model):
    product = models.ForeignKey(Products, related_name="variants", on_delete=models.CASCADE)
    variant_name = models.CharField(max_length=100)

    class Meta:
        db_table = "product_variant"
        unique_together = ("product", "variant_name")  

    def __str__(self):
        return self.variant_name
        
        
class SubVariant(models.Model):
    variant = models.ForeignKey(Variant, related_name="subvariants", on_delete=models.CASCADE)
    subvariant_name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "product_subvariant"
        unique_together = ("variant", "subvariant_name")  

    def __str__(self):
        return self.subvariant_name   