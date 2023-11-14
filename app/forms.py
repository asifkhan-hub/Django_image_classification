# image_prediction_app/forms.py
from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(
        label='Select an image',
        help_text='Supported formats: jpg, jpeg, png'
    )
