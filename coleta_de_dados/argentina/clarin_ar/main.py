# Importar bibliotecas
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pandas as pd


# Criando listas vazias para armazenar os dados

links_list = []
titulos_list = []

## Funções ##
  
def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

# Primeira página das últimas notícias("ultimo-momento") é diferente das demais! É preciso de uma extrair_infos para a primeira página e outro para as demais.
# A div que contém o conteúdo com as notícias altera de página para página. Precisamos encontrar um padrão que englobe todas as páginas. Tentando por 'ul' class=div1 que contém as 'li's das notícias. Erro: {NoneTupe object has no attribute finda_all}

def extrair_infos(url):
    html = acessar_pagina(url)
    conteudo = html.find('div',  'paywall_content')
    ul = conteudo.find_all('ul', 'class=div1')
    lista_noticia = ul.find_all('li')
    print(conteudo)
    '''
    for noticia in lista_noticia:

        # Extrai e monta os links
        link = noticia.a['href'].strip()
        link = f"https://www.clarin.com/ultimo-momento{link}"
        links_list.append(link)

        # Extrai titulos
        titulo_element = noticia.h2
        titulo = titulo_element.text.strip()
        titulos_list.append(titulo)
'''
def main():
    
    url = f'https://www.clarin.com/ultimo-momento/2'

    extrair_infos(url)
    
        
    #print("Links: \n", links_list, "\n \n Titulos: \n", titulos_list)

'''

i = 1
while extrair_infos is True:

    url = f'https://www.clarin.com/ultimo-momento/{i}'

    extrair_infos(url)
    
    i = i + 1
    
'''

if __name__ == "__main__":
    main()