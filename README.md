# GrabberToolAPI - Python

# Documentação!

## Eu fiz essa "API" sozinho portanto quero que entendam que ela tera varios erros e bugs inicialmente peço que me chamem nas rede socias em creditos.md

# Instalação

```console
git clone https://github.com/isqneeh/GrabberToolAPI.git
cd ./GrabberToolAPI
pip install -e .
```

# Em script
## CPF
```py
>>> import grabbertool
>>> consulta = grabbertool.search()
>>> resultado = consulta.cpf('12345678910')
>>> print(resultado)
# output
{...}
```

## CNPJ
```py
>>> import grabbertool
>>> consulta = grabbertool.search()
>>> resultado = consulta.cnpj('123456789101112')
>>> print(resultado)
# output
{...}
```

## CEP

```py
>>> import grabbertool
>>> consulta = grabbertool.search()
>>> resultado = consulta.cep('123456789')
>>> print(resultado)
# output
{...}
```
