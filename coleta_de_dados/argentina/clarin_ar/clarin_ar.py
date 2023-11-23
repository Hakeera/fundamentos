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
    conteudo = html.find('div',  'sc-a2d72323-0 hphvle')
    uls = conteudo.find_all('ul', 'div1')

    for ul in uls:
        lis = ul.find_all('li')
        for li in lis:

            link = li.a['href'].strip()
            links_list.append(f'https://www.clarin.com/ultimo-momento{link}')

            titulo = li.h2.text
            titulos_list.append(titulo)


def main():

    i = 2
    while True:
        url = f'https://www.clarin.com/ultimo-momento/page/{i}'
        variavel = requests.get(url)
        if variavel.status_code != 200:
            break

        acessar_pagina(url)

        extrair_infos(url)

        i = i + 1
        print("Links: \n", links_list, "\n \n Titulos: \n", titulos_list)


if __name__ == "__main__":
    main()
