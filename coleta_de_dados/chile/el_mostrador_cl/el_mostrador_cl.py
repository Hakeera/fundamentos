from bs4 import BeautifulSoup
import pandas as pd
import requests


# Criando listas vazias para armazenar os dados
links_list = []
titulos_list = []
subtitulos_list = []
datas_list = []
categorias = [
    'noticias',
    'pais',
    'mundo',
    'opnion',
    'mercados',
    'el-mostrador-radio',
    'destacados-cultura',
    'la-semana-politica-tv',
    'la-mesa',
    'cita-de-libros',
    'entrevistas'
]

## Funções ##

def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def extrair_infos(url):
    html = acessar_pagina(url)
    conteudo = html.find('div', 'd-section__body | common:margin-top-50')
    noticias = conteudo.find_all('div', 'd-tag-card | common:margin-top-25')
    
    for noticia in noticias:
        h4 = noticia.find('h4')
        # Titulos
        titulo = h4.text
        titulo_limpo = titulo.strip()
        titulos_list.append(titulo_limpo)
        # Links
        link = h4.a['href']
        links_list.append(link)
        # Data
        data = noticia.find('time').text
        datas_list.append(data)
        print("Titulos:\n", titulo_limpo, "Links:\n", link, "Datas:\n", data)


def main():
    for categoria in categorias:
        url = f"https://www.elmostrador.cl/categoria/{categoria}"
        extrair_infos(url)
        i = 2
        while True:
            url = f'https://www.elmostrador.cl/categoria/{categoria}/page/{i}/'
            try:
                extrair_infos(url)
            except:
                break
            i = i + 1   
    #print("Titulos:\n", titulos_list, "Links:\n", links_list, "Datas:\n", datas_list)


if __name__ == "__main__":
    main()
