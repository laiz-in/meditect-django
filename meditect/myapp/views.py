from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   return render(request, 'home.html')

def bmi(request):
   return render(request, 'bmi.html')

def diabeticdisease(request):
   return render(request, 'diabeticdisease.html')

def diabeticretinopathy(request):
   return render(request, 'diabeticretinopathy.html')

def heartdisease(request):
   return render(request, 'heartdisease.html')

def ReadMoreAboutAI(request):
   return render(request, 'ReadMoreAboutAI.html')

def skindisease(request):
   return render(request, 'skindisease.html')

def alzheimers(request):
   return render(request, 'alzheimers.html')

def ReadMoreAboutAI(request):
   return render(request, 'ReadMoreAboutAI.html')
