from django.db import models

# Create your models here.


class Reviews(models.Model):
    user_name = models.CharField(max_length=100)
    reviews_text = models.TextField()
    rating= models.IntegerField()
    
