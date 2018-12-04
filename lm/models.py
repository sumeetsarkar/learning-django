from django.db import models

# Create your models here.


# One to One Relationship - Conceptually Foreign key with unique True
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'Place: {self.name}'


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True
    )
    is_vegan = models.BooleanField(default=False)

    def __str__(self):
        return f'Restaurant: {self.name} , is_vegan: {self.is_vegan}'
