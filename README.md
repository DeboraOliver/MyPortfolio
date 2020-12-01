<h1>My Portfolio</h1>

## Como acessar:
Instale a versão 3.x do Python e o Virtualenv:
<ol>
<li>Clone este repositório : git clone https://github.com/DeboraOliver/MyPortfolio.git</li>
<li>Vá para o repositório : cd myportfolio</li>
<li>Crie um ambiente de desenvolvimento : virtualenv --python $( which python3 ) py3;</li>
<li>Instale as dependências : pip install -r requirements.txt;</li>
<li>Crie a base de dados : python manage.py migrate;</li>
<li>Suba o servidor : python manage.py runserver;</li>
<li>Acesse o programa em http://127.0.0.1:8000/</li>
</ol>