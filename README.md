# API-Rest-BookSwap

BookSwap é uma API RESTful desenvolvida em Django para facilitar a troca de livros entre usuários. O sistema permite que usuários cadastrem livros, façam avaliações (notas e comentários), enviem recomendações para outros usuários e gerenciem trocas de livros. A autenticação é baseada em JWT (JSON Web Tokens), e o projeto utiliza PostgreSQL como banco de dados.

Funcionalidades
Gerenciamento de Usuários: Cadastro e autenticação de usuários.
Livros: Cadastro, edição e exclusão de livros com informações como título, autor, condição e dono.
Avaliações: Usuários podem avaliar livros com notas (1 a 5) e comentários.
Recomendações: Envio de recomendações de livros para outros usuários.
Trocas: Sistema de troca de livros entre usuários com status (pendente, aceita, rejeitada, concluída).
Soft Delete: Exclusão lógica de registros (marcados como is_deleted=True).
Tecnologias Utilizadas
Python 3.12
Django 5.0
Django REST Framework (DRF)
PostgreSQL
Simple JWT para autenticação
drf-spectacular para documentação da API (Swagger/OpenAPI)
Pré-requisitos
Python 3.12+
PostgreSQL 16+
Git
Um ambiente virtual (recomendado)

Instalação
git clone https://github.com/Jvitorr-macedo/API-Rest-BookSwap.git
cd BookSwap

2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Instale as dependências
pip install -r requirements.txt

4. Configure o banco de dados
Crie um arquivo .env na raiz do projeto (BookSwap/) com as seguintes variáveis:

SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_NAME=bookswap_db
DATABASE_USER=seu_usuario_postgres
DATABASE_PASSWORD=sua_senha_postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432

5. Aplique as migrações
python manage.py makemigrations
python manage.py migrate

6. Inicie o servidor
python manage.py runserver
