from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Doc

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
  return render(request, 'dashboard.html', {}) 

def footer(request):
  return render(request, 'footer.html', {}) 