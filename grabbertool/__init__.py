'''
GrabberToolAPI
~~~~~~~~~~~~~~~~~~~~~

Um jeito simples agora!
Sobre a API:

    >>> import grabbertool
    >>> consulta = grabbertool.search()
    >>> resultado = consulta.cpf('12345678910')
    >>> print(resultado)
    {...}

    >>> import grabbertool
    >>> consulta = grabbertool.search()
    >>> resultado = consulta.cnpj('123456789101112')
    >>> print(resultado)
    {...}

    >>> import grabbertool
    >>> consulta = grabbertool.search()
    >>> resultado = consulta.cep('123456789')
    >>> print(resultado)
    {...}

:copyright: copy - Isqne 
'''
import grabbertool
from json.encoder import JSONEncoder
from urllib3.poolmanager import PoolManager
import json
import platform
import sys
import re
import base64
import requests
import os

class search(object):
    '''
    Sistema de busca da api
    ~~~~~~~~~~~~~~~~~~~~~~~
    Modo de uso:
        >>> import grabbertool from search
        >>> grabbertool.search.tipodebusca('1234567890')
    '''
    numpf=00000000000
    numep=00000000
    numpj=00000000000000
    version="1.0.0"

    def cpf(self, *args):
        numpf = self.numpf
        a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
        a=a.encode('ascii')
        a=base64.b64decode(a)
        a=a.decode('ascii')
        h={
        'Content-Type': "text/xml, application/x-www-form-urlencoded;charset=ISO-8859-1, text/xml; charset=ISO-8859-1",
        'Cookie': "ASPSESSIONIDSCCRRTSA=NGOIJMMDEIMAPDACNIEDFBID; FGTServer=2A56DE837DA99704910F47A454B42D1A8CCF150E0874FDE491A399A5EF5657BC0CF03A1EEB1C685B4C118A83F971F6198A78",
        'Host': "www.juventudeweb.mte.gov.br"
        }
        r=requests.post(a, headers=h, data=f'acao=consultar%20cpf&cpf={numpf}&nocache=0.7636039437638835').text
        cpf = re.search('NRCPF="(.*?)"', r).group(1)
        nome = re.search('NOPESSOAFISICA="(.*?)"', r).group(1).title()
        nascimento = re.search('DTNASCIMENTO="(.*?)"', r).group(1)
        nome_da_mae = re.search('NOMAE="(.*?)"', r).group(1).title()
        endereco = re.search('NOLOGRADOURO="(.*?)"', r).group(1).title()
        endereco_2 = re.search('NRLOGRADOURO="(.*?)"', r).group(1)
        complemento = re.search('DSCOMPLEMENTO="(.*?)"', r).group(1).title()
        bairro = re.search('NOBAIRRO="(.*?)"', r).group(1).title()
        cidade = re.search('NOMUNICIPIO="(.*?)"', r).group(1).title() + ',' + re.search('SGUF="(.*?)"', r).group(1)
        cep = re.search('NRCEP="(.*?)"', r).group(1)
        resultado = f'''
            CPF: {cpf}
            Nome: {nome}
            Nascimento: {nascimento}
            Nome da Mae: {nome_da_mae}
            Endereco: {endereco}
            Endereco_2: {endereco_2}
            Complemento: {complemento}
            Bairro: {bairro}
            Cidade: {cidade}
            CEP: {cep}
        '''
        return resultado

    def cep(self, *args):
        numep = self.numep
        url = f"https://ws.apicep.com/cep/{numep}.json"
        json: object = requests.get(url).json()
        cep = json["code"]
        resultado = f'''
            CEP:{json["code"]}
            Bairro:{json["district"]}
            Endereco:{json["address"]}
            Cidade:{json["city"]}
            Estado:{json["state"]}
        '''
        return resultado

    def cnpj(self, *args):
        numpj = self.numpj
        url = f'https://www.receitaws.com.br/v1/cnpj/{numpj}'
        cpj = requests.get(url).json()
        resultado = f'''
        Nome: {cpj["nome"]}
        Nome fantasia: {cpj["fantasia"]}
        Estado: {cpj["uf"]}
        Telefone: {cpj["telefone"]}
        Email: {cpj["email"]}
        Abertura: {cpj["abertura"]}
        Capital: {cpj["capital"]}
        Situação: {cpj["situacao"]}
        Municipio: {cpj["municipio"]}
        CEP: {cpj["cep"]}
        Bairro: {cpj["bairro"]}
        Porte: {cpj["porte"]}
        '''
        return resultado
