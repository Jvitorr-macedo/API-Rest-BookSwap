from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.models import Pessoa, Livro, Avaliacao, Recomendacao, Troca
from core.api.v1.serializers import PessoaSerializer, LivroSerializer, AvaliacaoSerializer, RecomendacaoSerializer, TrocaSerializer
from drf_spectacular.utils import extend_schema

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [AllowAny] 

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.filter(is_deleted=False)
    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticated] 
    http_method_names = ['get', 'post', 'put', 'delete']

    def perform_create(self, serializer):
        serializer.save() 

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.filter(is_deleted=False)
    serializer_class = AvaliacaoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(pessoa=self.request.user)

class RecomendacaoViewSet(viewsets.ModelViewSet):
    queryset = Recomendacao.objects.filter(is_deleted=False)
    serializer_class = RecomendacaoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(pessoa=self.request.user)

class TrocaViewSet(viewsets.ModelViewSet):
    queryset = Troca.objects.filter(is_deleted=False)
    serializer_class = TrocaSerializer
    permission_classes = [AllowAny] 

    @extend_schema(
        description="Cria ou gerencia uma troca de livros entre duas pessoas, sem necessidade de autenticação",
        responses={201: TrocaSerializer},
    )
    def perform_create(self, serializer):
        serializer.save()