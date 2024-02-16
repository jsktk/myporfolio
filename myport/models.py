from django.db import models

# Create your models here.

class mail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    
    
class Meta:
    db_table ="mail"