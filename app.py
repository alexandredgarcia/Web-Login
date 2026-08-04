'''
Aplicação Web Simples de Autenticação com Flask.

Este script demonstra uma estrutura básica de rotas, formulários POST/GET,
redirecionamento e mensagens temporárias (flash messages) usando o framework Flask.
'''

from flask import Flask, render_template, request, redirect, url_for, flash

# Inicialização da aplicação Flask
app = Flask(__name__)

# Configuração da chave secreta.
# A secret_key é necessária para usar mensagens 'flash' e sessões
app.secret_key = 'chave-temporaria-dev'

# Usuário fictício para testes
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "12345"

@app.route('/')
def home():
    '''
        Rota Raiz ('/').

        Redireciona automaticamente o usuário para a página de login.
    '''
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
        Rota de Autenticação ('/login').

        Suporta os métodos:
        - GET: Exibe o formulário de login (estado inicial).
        - POST: Processa os dados enviados pelo formulário e valida as credenciais.
    '''

    # Verifica se a requisição é do tipo POST (envio de formulário)
    if request.method == 'POST':
        # Captura os campos informados no formulário HTML
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        # Validação simples de credenciais
        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            # Envia mensagem de sucesso para ser exibida no template
            flash('Login realizado com sucesso!', 'success')
            # Renderiza a tela de login informando que o usuário está autenticado
            return render_template('login.html', logado=True, usuario=usuario)
        else:
            # Envia mensagem de erro
            flash('Usuário ou senha incorretos. Tente novamente.', 'danger')

    # Caso a requisição seja GET ou a autenticação falhe, exibe o formulário padrão
    return render_template('login.html', logado=False)

# Ponto de entrada
if __name__ == '__main__':
    # Executa o servidor de desenvolvimento do Flask com o modo debug ativo
    # O modo debug reinicia o servidor automaticamente ao alterar o código
    app.run(debug=True)