from django.shortcuts import render

def index(request):
	return render(request,'index.html')
def cita(request):
	return render(request,'cita.html')
def productos(request):
	return render(request,'productos.html')