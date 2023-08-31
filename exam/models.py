from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)



class Product(models.Model):
    name = models.TextField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()

products = Product.objects.all()







