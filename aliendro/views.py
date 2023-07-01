from django.http import HttpResponse

def saludo(request):    #Primer Vistazo
    return HttpResponse("Hola mundo, esto es un foro dedicado a Rodrigo Aliendro")

def despedida(request): #Dice adios
    return HttpResponse("Adios mundo, hasta la proxima")