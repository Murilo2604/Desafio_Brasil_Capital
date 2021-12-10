from selenium import webdriver
import requests

chrome = webdriver.Chrome("chromedriver.exe")

#-- CONSTELLATION ASSET MANAGEMENT
constellation_FIC_FIA = {
    'nome': 'Constellation Acoes FIC FIA',
    'codigo_AMBIMA': '517437',
    'rent_dia': '',
    'rent_ano': ''
}
chrome.get('https://constellation.com.br/pra-voce/')
# A tag 'section' que contem a tabela de rentabilidade dos fundos, possui id 'performance'
aux_c1 = chrome.find_element_by_id('performance')
aux_c2 = aux_c1.find_element_by_xpath('//table/tbody/tr[1]')
# As rentabilidades diaria e anual do fundo se encontram na 6a e 8a coluna da 1a linha da tabela, respectivamente
constellation_FIC_FIA['rent_dia'] = aux_c2.find_element_by_xpath('//td[6]').text
constellation_FIC_FIA['rent_ano'] = aux_c2.find_element_by_xpath('//td[8]').text

#-- NUCLEO CAPITAL
nucleo_FIC_FIA = {
    'nome': 'Nucleo Acoes FIC FIA',
    'codigo_AMBIMA': '296899',
    'rent_dia': '',
    'rent_ano': ''
}
chrome.get('https://www.nucleocapital.com.br/')
# A div que contem a tabela de rentabilidade do fundo e a 5a div do body do HTML
aux_n1 = chrome.find_element_by_xpath('//body/div[5]')
aux_n2 = aux_n1.find_element_by_xpath('//table/tbody/tr[1]')
# As rentabilidades diaria e anual do fundo se encontram na 3a e 6a coluna da 1a linha da tabela, respectivamente
nucleo_FIC_FIA['rent_dia'] = aux_n2.find_element_by_xpath('//td[3]').text
nucleo_FIC_FIA['rent_ano'] = aux_n2.find_element_by_xpath('//td[6]').text

#-- DYNAMO ASSET MANAGEMENT
dynamo_FIC_FIA = {
    'nome': 'Dynamo Cougar FIC FIA',
    'codigo_AMBIMA': '010431',
    'rent_dia': '',
    'rent_ano': ''
}
chrome.get('https://www.dynamo.com.br/pt')
# A tabela de rentabilidade possui id 'rentabilidade'
aux_d1 = chrome.find_element_by_id('rentabilidade')
# As rentabilidades diaria e anual do fundo se encontram na 6a e 9a coluna da 1a linha, respectivamente
dynamo_FIC_FIA['rent_dia'] = aux_d1.find_element_by_xpath('//tbody/tr[1]/td[6]').text
dynamo_FIC_FIA['rent_ano'] = aux_d1.find_element_by_xpath('//tbody/tr[1]/td[9]').text

fundos = [constellation_FIC_FIA, nucleo_FIC_FIA, dynamo_FIC_FIA]

for fundo in fundos:
    print("\n----", fundo['nome'], "----")
    print("Rent. Diária:", fundo['rent_dia'])
    print("Rent. Anual:", fundo['rent_ano'], "\n")

# Fechando a aba aberta pelo selenium
chrome.close()