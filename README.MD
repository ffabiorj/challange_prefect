# Challange prefect

## Como testar o projeto?

1. Clone o repositório.
2. Crie um virtualenv com python 3.11.9
3. Ative o virtualenv.
4. Instale as dependências.
5. Execute os testes.

```
git clone git@github.com:ffabiorj/challange_prefect.git
cd challange_prefect
python3 -m venv .venv
sourch .venv/bin/activate
pip install -r requirements.txt
python workflow.py
```

### Obs: As vezes para testar o timeout, tenha que rodar o script mais de uma vez.

## Para rodar o test

```
pytest
```

