from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework import viewsets
from projetfinal.serializers import MicrocontroleurSerializer
from quickstart.models import Microcontroleur

def index(request):
    return render(request, 'index.html')
#a ce niveau ces pour acceder a page web qui est externe a ma machine en fesant un POST
def Micro(request):
    if request.method == 'POST':
      uC = request.POST["uc"]
      Valeur = request.POST["value"]
      Date = request.POST["date"]
      print("Requeet Post\n")
      print(uC)
      print(Valeur)
      print(Date)
      #ceci represente l'enregistrement des donnees dans ma base de donnee
      microcontroleur = Microcontroleur()
      microcontroleur.nom = uC
      microcontroleur.modele = Valeur
      microcontroleur.serie = Date
      microcontroleur.save()
      #enregistre la derniere donnes capteer
      Microcontroleur.objects.all().delete()
      return HttpResponse('<h1>Success</h1>')   
    if request.method == 'GET':
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            todos = list(Microcontroleur.objects.all().values())
            return JsonResponse({'context': todos})

        #data = Microcontroleur.objects.all()
        #dataJson = MicrocontroleurSerializer(data, many = True)
        #return JsonResponse(dataJson.data, safe=False)  

class MicrocontroleurViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Microcontroleur.objects.all()
    serializer_class = MicrocontroleurSerializer
    #permission_classes = [permissions.IsAuthenticated]