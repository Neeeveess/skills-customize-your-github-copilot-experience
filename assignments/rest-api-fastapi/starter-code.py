"""
FastAPI Books API - Starter Code
Mergington High School - Computer Science

Este é o código inicial para a tarefa de construção de APIs REST com FastAPI.
Complete as tarefas seguindo as instruções no README.md

Para executar:
1. Instale as dependências: pip install fastapi uvicorn pydantic
2. Execute o servidor: uvicorn starter-code:app --reload
3. Acesse a documentação: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional

# Criar a aplicação FastAPI
app = FastAPI(
    title="Books API",
    description="API REST para gerenciar uma coleção de livros",
    version="1.0.0"
)

# TODO: Defina o modelo de dados Book usando Pydantic
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int = Field(gt=0, description="Ano de publicação deve ser positivo")
    genre: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "genre": "Ficção Científica"
            }
        }

# TODO: Defina o modelo BookUpdate para atualizações parciais
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = Field(None, gt=0)
    genre: Optional[str] = None

# Armazenamento em memória (lista de livros)
books_db: List[Book] = [
    Book(id=1, title="1984", author="George Orwell", year=1949, genre="Ficção Científica"),
    Book(id=2, title="Dom Casmurro", author="Machado de Assis", year=1899, genre="Romance"),
    Book(id=3, title="O Senhor dos Anéis", author="J.R.R. Tolkien", year=1954, genre="Fantasia")
]

# Contador para gerar IDs únicos
next_id = 4

# TODO: Tarefa 1 - Implemente o endpoint raiz
@app.get("/")
def read_root():
    """
    Endpoint raiz - mensagem de boas-vindas
    """
    return {
        "message": "Bem-vindo à Books API!",
        "docs": "/docs",
        "total_books": len(books_db)
    }

# TODO: Tarefa 3 - Implemente os endpoints CRUD

@app.get("/books", response_model=List[Book])
def get_books():
    """
    Listar todos os livros
    """
    # TODO: Implemente esta função
    pass

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """
    Obter detalhes de um livro específico
    """
    # TODO: Implemente esta função
    # Dica: Use HTTPException com status_code=404 se o livro não for encontrado
    pass

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: Book):
    """
    Adicionar um novo livro
    """
    # TODO: Implemente esta função
    # Dica: Use a variável global next_id para gerar IDs únicos
    pass

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate):
    """
    Atualizar um livro existente
    """
    # TODO: Implemente esta função
    # Dica: Atualize apenas os campos que foram fornecidos
    pass

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    """
    Remover um livro
    """
    # TODO: Implemente esta função
    pass

# TODO: Tarefa 4 - Implemente os endpoints de busca

@app.get("/books/search/", response_model=List[Book])
def search_books(
    author: Optional[str] = Query(None, description="Buscar por autor"),
    genre: Optional[str] = Query(None, description="Buscar por gênero")
):
    """
    Buscar livros por autor e/ou gênero
    """
    # TODO: Implemente esta função
    # Dica: Filtre a lista books_db baseado nos parâmetros fornecidos
    pass

# Para executar: uvicorn starter-code:app --reload
