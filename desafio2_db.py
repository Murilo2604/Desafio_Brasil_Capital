import requests

#-- URL DA API DA AMBIMA PARA SERIES HISTORICAS DE FUNDOS
API_AMBIMA = "https://api.anbima.com.br/feed/fundos/v1/fundos/{codigoFundo}/serie-historica"

#-- CONSTELLATION ASSET MANAGEMENT
constellation_FIC_FIA = {
    'nome': 'Constellation Acoes FIC FIA',
    'codigo_AMBIMA': '517437',
}

#-- NUCLEO CAPITAL
nucleo_FIC_FIA = {
    'nome': 'Nucleo Acoes FIC FIA',
    'codigo_AMBIMA': '296899',
}

#-- DYNAMO ASSET MANAGEMENT
dynamo_FIC_FIA = {
    'nome': 'Dynamo Cougar FIC FIA',
    'codigo_AMBIMA': '010431',
}

fundos = [constellation_FIC_FIA, nucleo_FIC_FIA, dynamo_FIC_FIA]

for fundo in fundos:
    url = API_AMBIMA.replace('{codigoFundo}', fundo['codigo_AMBIMA'])
    request = requests.get(url)
    print(url)
