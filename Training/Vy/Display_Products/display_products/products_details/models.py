from django.db import models

# Create your models here.



class ProductDetails(models.Model):
    id = models.AutoField(primary_key=True)
    nameProduct = models.CharField(max_length= 150)
    content = models.TextField()
    imgFile = models.CharField(max_length= 200)
    def __str__(self):
        self.id = str(self.id)
        return self.id
