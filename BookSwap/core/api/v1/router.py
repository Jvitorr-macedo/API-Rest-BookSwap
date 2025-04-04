from rest_framework.routers import DefaultRouter
from core.api.v1.viewsets import PessoaViewSet, LivroViewSet, AvaliacaoViewSet, RecomendacaoViewSet, TrocaViewSet

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet, basename='pessoa')
router.register(r'livros', LivroViewSet, basename='livro')
router.register(r'avaliacoes', AvaliacaoViewSet, basename='avaliacao')
router.register(r'recomendacoes', RecomendacaoViewSet, basename='recomendacao')
router.register(r'trocas', TrocaViewSet, basename='troca')