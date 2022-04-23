from django.db import models

class house(models.Model):
    nom = models.CharField(max_length= 300)   
    prenom = models.CharField(max_length= 300)
    emails = models.EmailField(max_length=300, null=True) 
    phone = models.FloatField(default=0)
   
def __str__(self):
    return self.nom

    
    


