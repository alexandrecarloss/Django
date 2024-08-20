from rest_framework import serializers

from adocao.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'proid', 
            'pronome', 
            'propreco', 
            'prosaldo', 
            'propetshop_ptsid', 
            'prodtvalidade', 
        )
    