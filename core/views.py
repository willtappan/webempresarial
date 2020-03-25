from django.shortcuts import render , HttpResponse

# Create your views here.
'''
Inici Home
Historia ABout
Servicios services 
Visitanos store
Contact
Blog 
Sambple

'''

'''
def home(request):
    return HttpResponse("Inicio")

def about(request):
    return HttpResponse("Historia")

def services(request):
    return HttpResponse("Servicios")
    
def store(request):
    return HttpResponse("visitanos")
def contact(request):
    return HttpResponse("Contacto")
def blog(request):
    return HttpResponse("Blog")
def sample(request):
    return HttpResponse("Sambple")
'''

def home(request):
    return render(request, "core/home.html")
def about(request):
    return render(request, "core/about.html")
def services(request):
    return render(request, "core/services.html")
def store(request):
    return render(request, "core/store.html")
