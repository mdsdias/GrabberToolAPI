from json.encoder import JSONEncoder
import requests
from urllib3.poolmanager import PoolManager
import json
import platform
import ssl
import sys
import re
import base64

class search(object):
    version="1.0.0"

    def cpf(self, cpf):
        a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
        a=a.encode('ascii')
        a=base64.b64decode(a)
        a=a.decode('ascii')
        h={
        'Content-Type': "text/xml, application/x-www-form-urlencoded;charset=ISO-8859-1, text/xml; charset=ISO-8859-1",
        'Cookie': "ASPSESSIONIDSCCRRTSA=NGOIJMMDEIMAPDACNIEDFBID; FGTServer=2A56DE837DA99704910F47A454B42D1A8CCF150E0874FDE491A399A5EF5657BC0CF03A1EEB1C685B4C118A83F971F6198A78",
        'Host': "www.juventudeweb.mte.gov.br"
        }
        r=requests.post(a, headers=h, data=f'acao=consultar%20cpf&cpf={cpf}&nocache=0.7636039437638835').text
        resultado = f'''
        -============///////=============-
        CPF: {re.search('NRCPF="(.*?)"', r).group(1)}
        Nome: {re.search('NOPESSOAFISICA="(.*?)"', r).group(1).title()}
        Nascimento: {re.search('DTNASCIMENTO="(.*?)"', r).group(1)}
        Nome da Mae: {re.search('NOMAE="(.*?)"', r).group(1).title()}
        Endereco: {re.search('NOLOGRADOURO="(.*?)"', r).group(1).title()}, {re.search('NRLOGRADOURO="(.*?)"', r).group(1)}
        Complemento: {re.search('DSCOMPLEMENTO="(.*?)"', r).group(1).title()}
        Bairro: {re.search('NOBAIRRO="(.*?)"', r).group(1).title()}
        Cidade: {re.search('NOMUNICIPIO="(.*?)"', r).group(1).title()}-{re.search('SGUF="(.*?)"', r).group(1)}
        CEP: {re.search('NRCEP="(.*?)"', r).group(1)}
        -============///////=============-
        '''
        return resultado

    def cep(self, cep):
        url = f"https://ws.apicep.com/cep/{cep}.json"
        json: object = requests.get(url).json()
        barrinha = '-============///////=============-'
        CEP = 'CEP:', json["code"]
        Bairro = 'Bairro:', json["district"]
        Endereco = 'Endereco:', json["address"] 
        Cidade = 'Cidade:', json["city"]
        Estado = 'Estado:', json["state"]
        resultado = f'''
        {barrinha}
        {CEP}
        {Bairro}
        {Estado}
        {Cidade}
        {Endereco}
        {barrinha}
        '''
        return resultado

    def cnpj(self, cnpj):
        url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
        cpj = requests.get(url).json()
        barrinha = '-============///////=============-'
        Nome = 'Nome:',cpj["nome"]
        Nome_Fantasia = 'Nome_Fantasia:',cpj["fantasia"]
        Estado = 'Estado:',cpj["uf"]
        Telefone = 'Telefone:', cpj["telefone"]
        Email = 'Email:', cpj["email"]
        Data_de_abertura = 'Data_de_abertura:', cpj["abertura"]
        Capital = 'Capital:', cpj["capital_social"]
        Situacao = 'Situacao:', cpj["situacao"]
        Municipio = 'Municipio:', cpj["municipio"]
        CEP = 'CEP', cpj["cep"]
        Bairro = 'Bairro:', cpj["bairro"]
        Porte = 'Porte:', cpj["porte"]
        resultado = f''' 
        {barrinha}
        {Porte}
        {Nome}
        {Nome_Fantasia}
        {Estado}
        {Telefone}
        {Email}
        {Data_de_abertura}
        {Capital}
        {Situacao}
        {Municipio}
        {Bairro}
        {CEP}
        {barrinha}
        '''
        return resultado