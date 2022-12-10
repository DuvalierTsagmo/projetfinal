
from rest_framework import serializers

from quickstart.models import Microcontroleur

#ceci est mon serialiseur avec les 3 champs de mon modeles
class MicrocontroleurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Microcontroleur
        fields = ['nom', 'modele', 'serie']