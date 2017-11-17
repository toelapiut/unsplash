from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    phone_number=models.CharField(max_length=14, blank=True)

    def __str__(self):
        return self.first_name
    class Meta:
        ordering=['first_name']

