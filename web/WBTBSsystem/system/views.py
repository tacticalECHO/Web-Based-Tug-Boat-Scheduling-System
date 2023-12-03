from django.shortcuts import render
from django.http import HttpResponse
from .models import Members
from django.template import loader
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the system index.")
def detail(request):
    memberlist=Members.objects.all()
    context={'memberlist':memberlist}
    return render(request, 'index.html', context)
def team(request):
    return render(request, 'index.html')