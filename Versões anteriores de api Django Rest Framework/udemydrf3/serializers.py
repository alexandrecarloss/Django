from rest_framework import serializers

from adocao.models import *

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = (
            'produto_proid',
            'servico_serid',
            'avadescricao',
            'avavalor',
            'pessoa_pesid',
            'avacod',
        )


class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = (
            'carid',
            'carpro',
            'carpes',
            'carser',
            'carquant',
            'carpreco',
        )

class FormapagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formapagamento
        fields = (
            'fpgid',
            'fpgdescricao',
        )


class ItemvendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemvenda
        fields = (
            'produto_proid',
            'itemvenda_venid',
            'itvqtde',
            'servico_serid', 
        )


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # 'logemail': {'write_only': True},
            'logsenha': {'write_only': True}
        }
        model = Login
        fields = (
            'logemail',
            'logsenha',
            'petshop_ptsid',
            'pessoa_pesid',
            'ong_ongid', 
        )


class NotafiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notafiscal
        fields = (
            'petshop_ptsid',
            'venda_venid',
            'ntfcod',
        )


class OngSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # 'ongemail': {'write_only': True},
        }
        model = Ong
        fields = (
            'ongid',
            'ongnome',
            'ongcidade',
            'ongbairro',
            'ongrua',
            'ongnum',
            'ongtelefone',
            'ongemail',
            'ongestado',
        )


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        # extra_kwargs = {
        #     'pesemail': {'write_only': True}
        # }
        model = Pessoa
        fields = (
            'pesid',
            'pescpf',
            'pesdtnascto',
            'pessexo',
            'pescidade',
            'pesbairro',
            'pesrua',
            'pesemail',
            'pesnumero',
            'pestelefone',
            'pesnome',
            'pesestado',
        )


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = (
            'petid',
            'petnome',
            'petsexo',
            'petcastrado',
            'petdtnascto',
            'petpeso',
            'pessoa_pesid',
            'pet_porte_ptpid',
            'pet_raca_ptrid',
            'pet_tipo_pttid',
        )


class PetAdocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetAdocao
        fields = (
            'ong_ongid',
            'pet_petid',
            'adoid',
        )


class PetFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetFoto
        fields = (
            'pftid',
            'pftfoto',
            'pet_petid',
        )


class PetPorteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetPorte
        fields = (
            'ptpid',
            'ptpnome',
            'ptpdescricao',
        )


class PetRacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetRaca
        fields = (
            'ptrid',
            'ptrnome',
            'pet_tipo_pttid',
        )


class PetTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetTipo
        fields = (
            'pttid',
            'pttnome',
        )


class PetshopSerializer(serializers.ModelSerializer):
    class Meta:
        # extra_kwargs = {
        #     'ptsemail': {'write_only': True}
        # }
        model = Petshop
        fields = (
            'ptsid',
            'ptsnome',
            'ptscnpj',
            'ptscidade',
            'ptsbairro',
            'ptsrua',
            'ptsnumero',
            'ptstelefone',
            'ptsemail',
            'ptsestado',
        )


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


class ProdutoFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoFoto
        fields = (
            'prfid',
            'prffoto',
            'produto_proid',
        )


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = (
            'serid',
            'servalor',
            'petshop_ptsid',
            'tiposervico_tpsid',
            'serdescricao',
        )


class ServicoFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoFoto
        fields = (
            'serftid',
            'serftvalor',
            'servico_serid',
        )


class SolicitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicita
        fields = (
            'pessoa_pesid',
            'servico_serid',
            'solid',
            'soldthr',
            'solpetid',
        )


class TiposervicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiposervico
        fields = (
            'tpsid',
            'tpsnome',
            'tpsdescricao',
        )


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = (
            'venid',
            'venser',
            'venpro',
            'venformapagamento_fpgid',
            'venpessoa_pesid',
            'venvalor',
        )


    
    
    
