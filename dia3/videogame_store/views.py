from rest_framework import viewsets
from .serializer import JogosSerializer, LojaSerializers, ClienteSerializer
from .models import Jogo, Loja, Cliente

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogosSerializer

class LojaViewSet (viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializers

class ClienteViewSet (viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer