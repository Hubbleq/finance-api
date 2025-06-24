# 💸 Finance API

API para controle financeiro pessoal desenvolvida em **Python**, utilizando **FastAPI**, **SQLModel** e **SQLite**.

Este projeto tem como objetivo o gerenciamento de contas, categorias e transações financeiras, permitindo controle de saldo, geração de relatórios e organização dos seus dados financeiros.

---

## 🚀 Tecnologias Utilizadas

- 🐍 Python 3.11+
- ⚡ FastAPI
- 🗄️ SQLModel + SQLite (ou PostgreSQL)
- 🔗 Uvicorn (servidor ASGI)
- 📦 Dependências gerenciadas via `requirements.txt`

---

## 📂 Estrutura do Projeto

```
app/
├── main.py                # Arquivo principal, inicia a API
├── database.py            # Configuração do banco de dados e sessão
├── models.py              # Modelos de dados (Account, Category, Transaction)
├── crud.py                # Operações CRUD (opcional, se criado)
└── routers/               # Rotas organizadas
    ├── accounts.py        # Rotas de contas
    ├── categories.py      # Rotas de categorias
    └── transactions.py    # Rotas de transações
requirements.txt            # Dependências do projeto
README.md                   # Documentação
```

---

## 🔧 Instalação e Execução Local

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. **Crie e ative um ambiente virtual:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**

```bash
uvicorn app.main:app --reload
```

5. **Acesse a documentação interativa:**

- Swagger UI → http://127.0.0.1:8000/docs
- Redoc → http://127.0.0.1:8000/redoc

---

## 📚 Funcionalidades

- ✅ Cadastro de contas financeiras
- ✅ Cadastro de categorias
- ✅ Registro de transações (receitas e despesas)
- ✅ Atualização automática do saldo da conta
- ✅ Filtros por data, tipo e categoria (em desenvolvimento)
- ✅ Geração de relatórios (em desenvolvimento)

---

## 🗄️ Modelagem de Dados

- **Account** → `id`, `name`, `balance`
- **Category** → `id`, `name`
- **Transaction** → `id`, `description`, `amount`, `date`, `type` (`income` ou `expense`), `account_id`, `category_id`

---

## 🏗️ Melhorias Futuras

- 🔐 Autenticação e autorização com JWT
- 📊 Relatórios avançados (gastos por categoria, fluxo mensal)
- 🚀 Deploy na nuvem (Render, Railway, Fly.io)
- 🧪 Testes automatizados (pytest + httpx)
- 🌐 Frontend para consumir essa API (React, Next.js ou outro)

---

## 🤝 Contribuição

Sinta-se livre para abrir issues, sugerir melhorias ou enviar pull requests.

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## ✨ Autor

Desenvolvido por **Bruno Cavalcante**  
[LinkedIn](https://www.linkedin.com/) • [Email](mailto:cavalcantebruno76@gmail.com)
