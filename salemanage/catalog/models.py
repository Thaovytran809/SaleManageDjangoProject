from django.utils import timezone
from django.db import models
from django.forms import ValidationError
from django.urls import reverse


# Create your models here.

class Catagory(models.Model):
    c_name = models.CharField(max_length=200, null=False, unique=False, verbose_name='category name')
    c_image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='category image')

    def get_absolute_url(self):
        return reverse("catagory_detail", args=[str(self.id)])
    def __str__(self):
        return self.c_name
class Product(models.Model):
    p_name = models.CharField(max_length=200, null=False, unique=False, verbose_name='product name')
    price = models.FloatField()
    p_image = models.ImageField(upload_to='images',null=True,blank=True, verbose_name='product image')
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True)

    def clean(self):
        if self.price<0:
            raise ValidationError('price can not be negative.')
    def save(self, *args, **kwargs):
        self.clean()
        super(Product, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("product_detail", args=[str(self.id)])
    def __str__(self):
        return self.p_name
class Customer(models.Model):
    cus_name = models.CharField(max_length=200, null=False, verbose_name='customer name')
    pkkh = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Catagory,help_text='select category for this customer')
    products = models.ManyToManyField(Product, help_text='select product for this customer')
    
    def get_absolute_url(self):
        return reverse("customer_detail", args=[str(self.id)])
    def __str__(self):
        return self.cus_name
    class Meta:
        ordering = ['created_date']
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, verbose_name='cus tomer name')
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, verbose_name='catagory name')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=' product name')
    count = models.IntegerField()
    total = models.FloatField(editable=False)
    created_date = models.DateTimeField()
    def clean(self):
        if self.product.catagory != self.catagory:
            raise ValidationError('The product dose not belong selected catagory')
        if self.count <0:
            raise ValidationError('Count can not be nagative')
    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.now()
        self.total = self.count * self.product.price
        super(Order, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("order_detail", args=[str(self.id)])
    def __str__(self):
        return f'{self.created_date}-{self.customer} ordered {self.count} of {self.product} in {self.catagory}'
    class Meta:
        ordering = ['created_date']
    



     
