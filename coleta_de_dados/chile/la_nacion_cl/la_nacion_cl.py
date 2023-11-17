from bs4 import BeautifulSoup
import pandas as pd
import requests


# Criando listas vazias para armazenar os dados
links_list = []
titulos_list = []
subtitulos_list = []
categorias = [
    'internacional',
    'nacional',
    'politica',
    'ciencia',
    'tecnologia',
    'dato-util',
    'entrevistas',
    'columnistas'
]


## Funções ##


def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def extrair_infos(url):
    html = acessar_pagina(url)
    conteudo = html.find('div', 'td-ss-main-content')
    cols = conteudo.find_all('div', 'td-block-span6')

    for col in cols:
        # Links
        links = col.a['href']
        links_list.append(links)

        # Títulos
        titulos = col.a['title']
        titulos_list.append(titulos)

        # Subtitulos
        '''subtitulos = col.p.text
        subtitulos_list.append(subtitulos)
'''

def main():
    
    # Looping para rodar lista de categorias
    for categoria in categorias:
        url = f'https://www.lanacion.cl/{categoria}/'
        extrair_infos(url)  # Primeira página (numeração vazia)
        print("Links: \n", links_list, "\n\n Titulos: \n", titulos_list, "\n\nSubtitulos: \n", subtitulos_list)
        
        # Looping para rodar número de páginas
        i = 2
        while True:
            url = f'https://www.lanacion.cl/{categoria}/page/{i}/'
            try:
                extrair_infos(url)
                print("Links: \n", links_list, "\n\n Titulos: \n", titulos_list, "\n\nSubtitulos: \n", subtitulos_list)
            except:
                break
            i = i + 1

if __name__ == "__main__":
    main()
