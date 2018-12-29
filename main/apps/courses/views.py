from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Courses

# Create your views here.
def index(request):
    context = {
        'courses' : Courses.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create(request):
    errors = Courses.objects.validate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)

    else:
        Courses.objects.create_course(request.POST)

    return redirect('/')

def remove(request, id):
    context = {
        'course' : Courses.objects.get(id=id)
    }
    return render(request, 'courses/deleteacourse.html', context)
    
def destroy(request, id):
    Courses.objects.delete_course(id)
    return redirect('index:index')
