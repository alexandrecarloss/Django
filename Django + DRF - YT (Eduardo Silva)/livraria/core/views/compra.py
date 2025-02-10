from rest_framework.viewsets import ModelViewSet
from core.serializers import CompraSerializer, CompraDetailSerializer, CriarEditarCompraSerializer
from core.models import Compra

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return CompraDetailSerializer
        return CriarEditarCompraSerializer
    
    def get_queryset(self):
        usuario = self.request.user
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)