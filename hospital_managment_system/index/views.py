from django.shortcuts import render, HttpResponse
from x.globalx import Globalx
# Create your views here.
def index(request):
    return render(request, "index.html")