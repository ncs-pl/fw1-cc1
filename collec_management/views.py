from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from collec_management.models import Collec

def about(request):
    return render(request, 'about.html')

def collection(request, n) :
    c = get_object_or_404(Collec, id=n)
    return render(request, 'collection.html', { 'collection': c })
