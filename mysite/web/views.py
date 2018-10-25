from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'MisPerris.html', {})

def registro(request):
    return render(request, 'Formulario.html', {})