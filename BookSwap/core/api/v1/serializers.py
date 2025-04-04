# core/api/v1/serializers.py
from rest_framework import serializers
from core.models import Pessoa, Livro, Avaliacao, Recomendacao, Troca

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        pessoa = Pessoa.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return pessoa

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'pessoa', 'titulo', 'autor', 'condicao', 'livro_id', 'created_at', 'updated_at']

class AvaliacaoSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='livro.pessoa', read_only=True)
    livro = serializers.CharField(source='livro.titulo', read_only=True)
    livro_id = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.filter(is_deleted=False), 
    source='livro', write_only=True)

    class Meta:
        model = Avaliacao
        fields = ['usuario', 'livro', 'livro_id', 'nota', 'comentario', 'created_at']

class RecomendacaoSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='livro.pessoa', read_only=True)
    livro = serializers.CharField(source='livro.titulo', read_only=True)
    livro_id = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.filter(is_deleted=False), 
    source='livro', write_only=True)

    class Meta:
        model = Recomendacao
        fields = ['usuario', 'livro', 'livro_id', 'texto', 'created_at']  # Removido 'destinatario_nome'

class TrocaSerializer(serializers.ModelSerializer):
    solicitante_nome = serializers.CharField(source='livro_solicitante.pessoa', read_only=True)
    receptor_nome = serializers.CharField(source='livro_receptor.pessoa', read_only=True)
    livro_solicitante_id = serializers.CharField(source='livro_solicitante.livro_id', read_only=True)
    livro_solicitante_titulo = serializers.CharField(source='livro_solicitante.titulo', read_only=True)
    livro_solicitante_condicao = serializers.CharField(source='livro_solicitante.condicao', read_only=True)
    livro_receptor_id = serializers.CharField(source='livro_receptor.livro_id', read_only=True)
    livro_receptor_titulo = serializers.CharField(source='livro_receptor.titulo', read_only=True)
    livro_receptor_condicao = serializers.CharField(source='livro_receptor.condicao', read_only=True)

    livro_solicitante = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.filter(is_deleted=False), write_only=True)
    livro_receptor = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.filter(is_deleted=False), write_only=True)

    class Meta:
        model = Troca
        fields = [
            'id', 
            'solicitante_nome', 
            'receptor_nome', 
            'livro_solicitante', 'livro_solicitante_id', 'livro_solicitante_titulo', 'livro_solicitante_condicao',
            'livro_receptor', 'livro_receptor_id', 'livro_receptor_titulo', 'livro_receptor_condicao',
            'status', 'created_at', 'updated_at'
        ]

    def validate(self, data):
        livro_solicitante = data['livro_solicitante']
        livro_receptor = data['livro_receptor']
        if livro_solicitante.pessoa == livro_receptor.pessoa:
            raise serializers.ValidationError("A troca não pode ser feita entre a mesma pessoa.")
        return data