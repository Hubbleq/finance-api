# Finance API

API para controle financeiro pessoal desenvolvida em Python, utilizando FastAPI, SQLModel e SQLite.

Este projeto tem como objetivo o gerenciamento de contas, categorias e transações financeiras, permitindo controle de saldo, geração de relatórios e organização dos dados financeiros.

## Tecnologias Utilizadas

- Python 3.11+
- FastAPI
- SQLModel + SQLite
- Uvicorn (servidor ASGI)

## Estrutura do Projeto

```
app/
├── main.py                # Arquivo principal, inicia a API
├── database.py            # Configuração do banco de dados e sessão
├── models.py              # Modelos de dados (Account, Category, Transaction)
├── crud.py                # Operações CRUD (opcional)
└── routers/               # Rotas organizadas
    ├── accounts.py        # Rotas de contas
    ├── categories.py      # Rotas de categorias
    └── transactions.py    # Rotas de transações
requirements.txt            # Dependências do projeto
README.md                   # Documentação
```

## Instalação e Execução Local

1. Clone o repositório:

```
git clone https://github.com/Hubbleq/finance-api.git
cd finance-api
```

2. Crie e ative um ambiente virtual:

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Execute a aplicação:

```
uvicorn app.main:app --reload
```

5. Acesse a documentação interativa:

- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

## Funcionalidades

- Cadastro de contas financeiras
- Cadastro de categorias
- Registro de transações (receitas e despesas)
- Atualização automática do saldo da conta
- Filtros por data, tipo e categoria (em desenvolvimento)
- Geração de relatórios (em desenvolvimento)

## Modelagem de Dados

- Account: id, name, balance
- Category: id, name
- Transaction: id, description, amount, date, type (income ou expense), account_id, category_id

## Melhorias Futuras

- Autenticação e autorização com JWT
- Relatórios avançados (gastos por categoria, fluxo mensal)
- Deploy na nuvem (Render, Railway, Fly.io)
- Testes automatizados (pytest + httpx)
- Desenvolvimento de frontend para consumir a API

## Contribuição

Contribuições são bem-vindas. Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

## Autor

Bruno Cavalcante  
Email: cavalcantebruno76@gmail.com  
LinkedIn: https://www.linkedin.com/in/bruno-xz/
