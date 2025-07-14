# 💸 Finance API

> Projeto pessoal para controle de finanças, desenvolvido em Java com Spring Boot.

---

## 📚 Sobre o Projeto

O **Finance API** é uma aplicação backend simples para gerenciamento financeiro pessoal.  
Ela permite o cadastro de receitas e despesas, além de possibilitar consultas e cálculos de saldo.

Este projeto tem como objetivo estudar e aplicar boas práticas em **Java**, **Spring Boot** e **arquitetura de APIs RESTful**, além de servir como um portfólio pessoal.

---

## 🚀 Tecnologias utilizadas

- Java 17
- Spring Boot 3
- Spring Web
- Spring Data JPA
- Banco H2 (em memória)
- Lombok
- Maven

---

## ✅ Funcionalidades

- [x] Cadastro de transações financeiras
- [x] Listagem de transações
- [ ] Filtro por tipo (receita/despesa)
- [ ] Filtro por data
- [ ] Cálculo automático de saldo
- [ ] Exportação de relatório (CSV/JSON)
- [ ] Validação de campos com Bean Validation
- [ ] Integração com frontend ou documentação via Swagger

---

## 🧠 Modelo de dados

```json
{
  "id": 1,
  "description": "Salário",
  "amount": 5000.00,
  "date": "2025-07-14",
  "type": "INCOME"
}


📂 Como rodar localmente
Pré-requisitos
Java 17+

Maven 3.8+

Git instalado

Passos
bash
Copiar
Editar
# Clone o repositório
git clone https://github.com/hubbleq/finance-api.git
cd finance-api

# Rode o projeto
./mvnw spring-boot:run
A aplicação estará disponível em:

arduino
Copiar
Editar
http://localhost:8080/
🔎 Exemplos de uso
▶️ Criar transação
http
Copiar
Editar
POST /transactions
Content-Type: application/json
json
Copiar
Editar
{
  "description": "Mercado",
  "amount": 250.00,
  "date": "2025-07-13",
  "type": "EXPENSE"
}
📥 Listar transações
http
Copiar
Editar
GET /transactions
🔒 Banco de dados H2
Você pode visualizar os dados acessando:

bash
Copiar
Editar
http://localhost:8080/h2-console
Configuração padrão:

JDBC URL: jdbc:h2:mem:finance

Username: sa

Password: (em branco)

📌 Estrutura inicial
bash
Copiar
Editar
finance-api
├── controller
├── model
├── repository
├── resources/
│   └── application.properties
└── FinanceApiApplication.java
👨‍💻 Autor
Bruno Cavalcante Pires
Estudante de Ciência da Computação (4º semestre) — UNIP
LinkedIn • GitHub

📝 Licença
Este projeto é de uso educacional e pessoal.
Sinta-se à vontade para estudar, melhorar e reutilizar com créditos ao autor.

yaml
Copiar
Editar

---

## ✅ Como usar

1. Copie esse conteúdo para um arquivo `README.md` na raiz do seu projeto:

```bash
touch README.md
Cole o conteúdo e salve.

Faça commit e push:

bash
Copiar
Editar
git add README.md
git commit -m "Adiciona README com descrição do projeto"
git push
