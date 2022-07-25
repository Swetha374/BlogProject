from django.db import models

# Create your models here.


class Blogs(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    liked_by=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Mobiles(models.Model):
    name=models.CharField(max_length=50,unique=True)
    price=models.PositiveIntegerField(default=6000)
    band=models.CharField(max_length=50,default="4g")
    display=models.CharField(max_length=120)
    processor=models.CharField(max_length=120)

    def __str__(self):
        return self.name





