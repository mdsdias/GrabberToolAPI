<p align="center">
    <img style="border-radius: 50%;" src="https://imgur.com/iYkqIWM.gif" width="150px" alt="gif">
    <h1 align="center">GrabberToolAPI</h1>
</p>

<div>
    <p>
        <center>
            <div align="right">
                <img style="border-radius: 20%;" src="https://imgur.com/iYkqIWM.png" min-width="100px" max-width="150px" width="150px" align="right" alt="icon">
            </div>
            <div align="left">
                <br /><h2>Docs da verção em <a href="https://github.com/Isqneeh/GrabberTool">PythonScript!</h2><br /></a>
                <br /><h2><a href="https://github.com/Isqneeh/GrabberTool-WebSite"> Site </a> Oficial do GrabberTool</h2><br /></a>
            </div>
        </center>
    </p>
</div>

# Documentação!

<h2> Eu fiz essa "API" sozinho portanto quero que entendam que ela tera varios erros e bugs inicialmente peço que me chamem nas rede socias no final do readme </h2>

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
