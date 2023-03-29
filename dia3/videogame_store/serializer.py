from rest_framework import serializers
from .models import Jogo, Loja

class JogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = ['nome', 'preco']

class JogosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['nome', 'endereco', 'telefone']