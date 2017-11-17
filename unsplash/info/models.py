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
    
    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()

class tags(models.Model):
    name=models.CharField(max_length=10)
    tag_image=models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['name']

    #saving function
    def save_tag(self):
        self.save()

    #deleting function
    def delete_tag(self):
        self.delete()
