from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Doc, Predictions
from django.db import models

# Create your views here.

def index(request):
  return render(request, 'index.html', {}) 

def file_upload_view(request):
  print(request.FILES)
  if request.method == 'POST':
    my_file = request.FILES.get('file')
    Doc.objects.create(upload = my_file)
    return HttpResponse('')
  return JsonResponse({'post':'false'})

def about(request):
  return render(request, 'about.html', {}) 

def dashboard(request):
  # Get all predictions from the database
  predictions = Predictions.objects.all()
  
  # Calculate accuracy
  total_predictions = predictions.count()
  total_conformity = predictions.filter(conformity=True).count()
  accuracy = total_conformity / total_predictions * 100 if total_predictions > 0 else 0
  accuracy_formatted = "{:.1f}".format(accuracy)
  
  # Calculate average time of response
  total_response_time = predictions.aggregate(models.Sum('t_response'))['t_response__sum']
  average_response_time = total_response_time / total_predictions if total_predictions > 0 else 0
  average_response_time_formatted = "{:.1f}".format(average_response_time)

  # Pass the data to the template
  context = {
      'predictions': predictions,
      'accuracy': accuracy_formatted,
      'average_response_time': average_response_time_formatted,
      # Include any additional data in the context
      # ...
  }

  return render(request, 'dashboard.html', context) 

def footer(request):
  return render(request, 'footer.html', {}) 