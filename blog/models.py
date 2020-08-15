from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='blog/image')
    upload_date = models.DateField()


    def __str__(self):
        return self.title