from django.contrib import admin
from core.models import Pessoa, Livro, Avaliacao, Recomendacao, Troca

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'pessoa', 'condicao', 'livro_id']

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['livro', 'pessoa', 'nota', 'created_at']

@admin.register(Recomendacao)
class RecomendacaoAdmin(admin.ModelAdmin):
    list_display = ['livro', 'pessoa', 'texto', 'created_at']

@admin.register(Troca)
class TrocaAdmin(admin.ModelAdmin):
    list_display = ['get_solicitante_nome', 'get_receptor_nome', 'livro_solicitante', 'livro_receptor', 'status']

    def get_solicitante_nome(self, obj):
        return obj.livro_solicitante.pessoa
    get_solicitante_nome.short_description = 'Solicitante'

    def get_receptor_nome(self, obj):
        return obj.livro_receptor.pessoa
    get_receptor_nome.short_description = 'Receptor'