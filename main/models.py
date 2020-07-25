from django.db import models

#Create your models here
class FoodModel(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="pics", verbose_name="")

    def __str__(self):
        return self.name + ":" + str(self.image)
    