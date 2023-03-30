from rest_framework import serializers
from .models import Jogo, Loja, Cliente

class JogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = ['nome', 'preco']


class LojaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['nome', 'endereco', 'telefone']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'telefone']