from django.db import models

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=255, null=True)
    mainphoto = models.ImageField(blank=True, null=True, upload_to='')
    contents = models.TextField()
    
    def __str__(self):
        return self.postname