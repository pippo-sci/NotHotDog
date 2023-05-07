from django.urls import path, include
from . import views
from NotHotDogWebsite.views import index, file_upload_view

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('footer', views.footer, name='footer'),
    path('upload/', file_upload_view, name='upload-view')
]
