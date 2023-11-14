# # image_prediction_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageUploadForm
from .predict import predict_and_save_image
from .models import PredictedImage

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            prediction = predict_and_save_image(uploaded_image)
            predicted_image = PredictedImage.objects.filter(prediction=prediction).last()

            response_data = {
                'prediction': prediction,
                'predicted_image': predicted_image.image.url if predicted_image else None,
            }

            return JsonResponse(response_data)
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})
