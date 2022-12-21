from django.db import models

# Create your models here.



class Kategori(models.Model):
    name = models.CharField(max_length=100)

class Filmler(models.Model):
    film_adı = models.CharField(max_length=200)
    film_acıklama = models.TextField()
    film_resmi = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)
    