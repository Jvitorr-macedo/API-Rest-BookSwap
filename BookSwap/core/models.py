from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

class Pessoa(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

class Livro(BaseModel):
    pessoa = models.CharField(max_length=100)  # Mantido como CharField conforme seu exemplo
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    condicao = models.CharField(
        max_length=50,
        choices=[('novo', 'Novo'), ('usado_bom', 'Usado - Bom'), ('usado_regular', 'Usado - Regular')]
    )
    livro_id = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

class Avaliacao(BaseModel):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='avaliacoes')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)  # Quem fez a avaliação
    nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Apenas nota
    comentario = models.TextField(blank=True)  # Apenas comentário sobre o livro

    class Meta:
        unique_together = ('livro', 'pessoa')
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

class Recomendacao(BaseModel):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='recomendacoes')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)  # Quem fez a recomendação
    texto = models.TextField()  # Texto da recomendação

    class Meta:
        unique_together = ('livro', 'pessoa')
        verbose_name = 'Recomendação'
        verbose_name_plural = 'Recomendações'

class Troca(BaseModel):
    livro_solicitante = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='trocas_solicitante')
    livro_receptor = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='trocas_receptor')
    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente', 'Pendente'),
            ('aceita', 'Aceita'),
            ('rejeitada', 'Rejeitada'),
            ('concluida', 'Concluída')
        ],
        default='pendente'
    )

    class Meta:
        verbose_name = 'Troca'
        verbose_name_plural = 'Trocas'
        unique_together = ('livro_solicitante', 'livro_receptor')