from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(4)])
    second_name = models.CharField(max_length=60, validators=[MinLengthValidator(4)])
    feedback = models.TextField()
    rating = models.PositiveIntegerField()