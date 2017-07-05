from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User) # La liaison OneToOne vers le modèle User
    telephone = models.IntegerField(null=True)
    benevole = models.BooleanField(default=False)
    adresse = TextField(null=True, blank=True)
    
    def __unicode__(self):
        return u"Profil de {0}".format(self.user.username)

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return u"Catégorie de compétences {0}".format(self.nom)

class Details(models.Model):
    details = models.TextField()
    user = models.ForeignKey('Profil')
    categorie = models.ManyToManyField('Categorie')

