from django.db import models

#creation de mon modele microcontroleur avec mes trois tables
class Microcontroleur(models.Model):
    nom = models.fields.CharField(max_length=100)
    modele = models.fields.CharField(max_length=10)
    serie = models.fields.CharField(max_length=10)