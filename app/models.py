# image_prediction_app/models.py
from django.db import models

class PredictedImage(models.Model):
    prediction = models.CharField(max_length=255)
    image = models.ImageField(upload_to='predicted_images/')

    def __str__(self):
        return f"{self.prediction} - {self.image.name}"
