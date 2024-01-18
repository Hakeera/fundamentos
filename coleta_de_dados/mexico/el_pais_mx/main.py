# Importar bibliotecas
from bs4 import BeautifulSoup
import pandas as pd
import requests


# Criando listas vazias para armazenar os dados

links_list = []
titulos_list = []

## Funções ##


def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def extrair_infos(url):
    html = acessar_pagina(url)
    conteudo = html.find('div',  'z z-hi')
    print(conteudo)


def main():
    
    url = f'https://elpais.com/mexico/actualidad/'
    variavel = requests.get(url)

    extrair_infos(url)


if __name__ == "__main__":
    main()
