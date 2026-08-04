## 🔐 Sistema de Login com Flask

Uma aplicação web simples desenvolvida com Python e Flask para demonstrar os conceitos fundamentais de autenticação, manipulação de rotas, formulários HTML, requisições HTTP (GET e POST) e mensagens temporárias (Flash Messages).
Objetivo: Projeto desenvolvido para fins de estudo e prática do framework Flask.

---

## 📌 Funcionalidades

- Página inicial com redirecionamento automático para o login.
- Formulário de autenticação utilizando os métodos GET e POST.
- Validação de usuário e senha.
- Exibição de mensagens de sucesso e erro utilizando Flash Messages.
- Renderização dinâmica da página após autenticação.
- Estrutura simples para servir de base para projetos maiores.


---

## 🛠️ Tecnologias Utilizadas
Python 3.x
Flask
HTML (Templates Jinja2)

---

## 📂 Estrutura do Projeto
```text
projeto-login/
│
├── app.py
├── templates/
│   └── login.html
```

---

## 🔑 Credenciais para Teste
```text
Campo	Valor
Usuário	admin
Senha	12345
```

---

## 📖 Conceitos Demonstrados

Este projeto aborda os seguintes conceitos do Flask:

- Criação de aplicações Flask
- Rotas (@app.route)
- Redirecionamentos (redirect e url_for)
- Templates com Jinja2
- Requisições HTTP (GET e POST)
- Manipulação de formulários (request.form)
- Flash Messages (flash)
- Configuração de secret_key
- Estrutura básica para autenticação

---

## ⚠️ Observação

Este projeto possui finalidade exclusivamente educacional.

As credenciais estão definidas diretamente no código apenas para fins de demonstração. Em aplicações reais, recomenda-se:

- armazenar senhas utilizando hash (por exemplo, werkzeug.security);
- utilizar banco de dados para gerenciamento de usuários;
- implementar sessões de usuário;
- proteger a aplicação contra ataques como CSRF e força bruta;
- utilizar variáveis de ambiente para informações sensíveis.


---

## 🚀 Possíveis Melhorias

- Cadastro de usuários
- Recuperação de senha
- Banco de dados SQLite ou PostgreSQL
- Sistema de sessões
- Logout


---


