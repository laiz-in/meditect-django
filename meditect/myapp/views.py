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
   if request.method == 'POST' and request.FILES.get('image'):
         # Get the uploaded image from the request
         uploaded_image = request.FILES['image']
         
         # Process the image (your image processing logic goes here)
         # For demonstration purposes, let's assume the result is a simple text string
         result_text = "This is the result of image processing."

         # Send the result_text as a response
         return render(request, 'alzheimers.html', {'result_text': result_text})

      # If it's a GET request or no image was uploaded yet, render the empty form
   return render(request, 'alzheimers.html')



def ReadMoreAboutAI(request):
   return render(request, 'ReadMoreAboutAI.html')
