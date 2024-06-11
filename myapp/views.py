from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def login(request):
    return render(request,"login.html",{})
def index(request):
    return render(request,"index.html")
def asesorias(request):
    return render(request,"asesorias.html")
def charlasOV(request):
    return render(request,"charlasOV.html")
def charts(request):
    return render(request,"charts.html")
def defineTuFuturo(request):
    return render (request,"defineTuFuturo.html")
def seguimientoCienciasBasicas(request):
    return render (request,"seguimientoCienciasBasicas.html")
def seguimientoNivelacion(request):
    return render (request,"seguimientoNivelacion.html")
def tables(request):
    return render (request,"tables.html")
def talleres(request):
    return render(request,"talleres.html")
def search (request):
    return render (request,"search.html")

