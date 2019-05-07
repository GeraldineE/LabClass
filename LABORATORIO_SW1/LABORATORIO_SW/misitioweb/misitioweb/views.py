from django.http import HttpResponse
from django.shortcuts import render

def holamundo(request):
   return render (request, 'home.html')

   # return HttpResponse("Hello World!")