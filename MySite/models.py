from django.db import models

# Create your models here.
class TimespantedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
        
        
class ContactModel(TimespantedModel):
    name = models.CharField(max_length=50)
    number  = models.CharField(max_length=50)
    email = models.CharField( max_length=254)
    message = models.CharField( max_length=300)

    def __str__(self):
        return self.name
    