from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=150,verbose_name="Category Title")
    slug=models.SlugField(max_length=55,verbose_name="Category Slug")
    category_image=models.ImageField(upload_to='category',blank=True,null=True,verbose_name="Category Image")
    is_active=models.BooleanField(verbose_name="Is Active?")
    is_featured=models.BooleanField(verbose_name="Is Featured?")


    def __str__(self):
        return self.title
class product(models.Model):
    
    title=models.CharField(max_length=150,verbose_name="Product Title")   
    slug=models.SlugField(max_length=160,verbose_name="Product slug")
    description=models.TextField(verbose_name="Short Description")
    product_image=models.ImageField(upload_to='product',blank=True,null=True,verbose_name="Product image") 
    price=models.DecimalField(max_digits=8,decimal_places=2)    
    productStock=models.PositiveIntegerField()
    category=models.ForeignKey(Category,verbose_name="product_category",on_delete=models.CASCADE)
    is_active=models.BooleanField(verbose_name="Is Active")
    is_featured=models.BooleanField(verbose_name="Is Featured")


    def __str__(self):
        return self.title

class Relatedimage(models.Model):
    products=models.ForeignKey(product,default=None,on_delete=models.CASCADE)
    image=models.FileField(upload_to='relimg',null=True)

class Cart(models.Model):
    user=models.ForeignKey(User,verbose_name="User",on_delete=models.CASCADE)
    products=models.ForeignKey(product,verbose_name="Poduct",on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1,verbose_name="Quantity")

    def __str__(self):
        return str(self.user)

    @property
    def total_price(self):
        return self.quantity*self.products.price
