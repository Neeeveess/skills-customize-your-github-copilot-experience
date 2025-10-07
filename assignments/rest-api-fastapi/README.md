# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você vai aprender a construir uma API REST completa usando o framework FastAPI do Python. Você criará endpoints para gerenciar uma coleção de livros, incluindo operações CRUD (Create, Read, Update, Delete) e aprenderá sobre validação de dados, documentação automática e melhores práticas de desenvolvimento de APIs.

## 📝 Tasks

### 🛠️	Tarefa 1: Configurar o Projeto FastAPI

#### Description
Configure o ambiente de desenvolvimento e crie a estrutura básica da aplicação FastAPI. Você deve instalar as dependências necessárias e criar um servidor básico que responda a requisições HTTP.

#### Requirements
Completed program should:

- Instalar FastAPI e Uvicorn usando pip
- Criar uma aplicação FastAPI básica
- Implementar um endpoint raiz (`/`) que retorne uma mensagem de boas-vindas
- Executar o servidor e verificar que está funcionando corretamente
- Acessar a documentação automática em `/docs`


### 🛠️	Tarefa 2: Criar Modelo de Dados para Livros

#### Description
Defina os modelos de dados usando Pydantic para representar livros. Isso garantirá que os dados recebidos pela API sejam validados automaticamente.

#### Requirements
Completed program should:

- Criar uma classe `Book` usando Pydantic BaseModel
- Incluir campos: id (int), título (str), autor (str), ano de publicação (int), gênero (str)
- Adicionar validações apropriadas (ex: ano deve ser positivo)
- Criar um modelo opcional `BookUpdate` para atualizações parciais


### 🛠️	Tarefa 3: Implementar Endpoints CRUD

#### Description
Crie endpoints RESTful para todas as operações CRUD de livros. Use métodos HTTP apropriados (GET, POST, PUT, DELETE) e códigos de status HTTP corretos.

#### Requirements
Completed program should:

- `GET /books` - Listar todos os livros
- `GET /books/{id}` - Obter detalhes de um livro específico
- `POST /books` - Adicionar um novo livro
- `PUT /books/{id}` - Atualizar um livro existente
- `DELETE /books/{id}` - Remover um livro
- Retornar códigos de status HTTP apropriados (200, 201, 404, etc.)
- Implementar tratamento de erros para livros não encontrados


### 🛠️	Tarefa 4: Adicionar Funcionalidades de Busca

#### Description
Implemente endpoints adicionais para buscar e filtrar livros com base em diferentes critérios.

#### Requirements
Completed program should:

- `GET /books/search?author=nome` - Buscar livros por autor
- `GET /books/search?genre=genero` - Buscar livros por gênero
- Permitir combinação de múltiplos parâmetros de busca
- Retornar lista vazia se nenhum livro for encontrado
- Testar todos os endpoints usando a documentação interativa do FastAPI


## 💡 Tips

- Use a documentação automática do FastAPI em `/docs` para testar seus endpoints
- Comece com uma lista em memória para armazenar os livros antes de considerar um banco de dados
- Preste atenção aos códigos de status HTTP - eles comunicam o resultado da operação
- Use type hints do Python para melhor validação e documentação automática
- Teste cada endpoint após implementá-lo antes de passar para o próximo

## 📚 Resources

- [Documentação Oficial do FastAPI](https://fastapi.tiangolo.com/)
- [Tutorial FastAPI](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## 🎓 Learning Goals

Ao completar esta tarefa, você será capaz de:
- Construir APIs REST profissionais usando FastAPI
- Validar dados de entrada usando Pydantic
- Implementar operações CRUD completas
- Usar métodos HTTP e códigos de status apropriadamente
- Testar APIs usando documentação interativa
- Entender os princípios de design de APIs RESTful
