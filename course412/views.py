from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def git_learn(request):
    return render(request, "gl.html")