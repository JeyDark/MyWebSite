from django.urls import path
from .views import *
app_name = "MySite"

urlpatterns = [
    path('home', Home, name="home"),
    path('project/', Projects, name="project"),
    path('resume/', Resume, name="resume"),
    path('contact/', Contact, name="contact"),
    #path('generate-pdf/', generate_pdf, name='generate_pdf'),
    path('generate-pdf/', generate_pdf2, name='generate_pdf'),
] 
