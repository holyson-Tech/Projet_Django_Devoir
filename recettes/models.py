from django.db import models

# Create your models here.

class Recette(models.Model):
    date = models.DateField
    description = models.TextField()
    montant = models.FloatField()

def __str__(self):
        return f"{self.description} au prix de : {self.prix} FCFA "