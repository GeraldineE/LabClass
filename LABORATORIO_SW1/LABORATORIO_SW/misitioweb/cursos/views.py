from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.
def Lista_De_Cursos(request):
    courses = Curso.objects.all()
    #Response = ', '.join([str (course)for cursos in Course])
    #return HttpResponse(Response)
    return render(request, 'courses/listadecursos.html', {'courses': courses})

def course_detail(request, pk):
    course = Curso.objects.get(pk=pk)
    return render(request, 'courses/curso_detail.html',{'course':course})