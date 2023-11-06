# Importar bibliotecas
from bs4 import BeautifulSoup
import requests


## Funções ##

# Criando listas vazias para armazenar os dados

links_list = []
titulos_list = []


def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def extrair_infos(url):
    html = acessar_pagina(url)
    conteudo = html.find('div', attrs={'class': 'breaking-news'})
    lista_noticia = conteudo.find_all('article')

    for noticia in lista_noticia:

        # Extrai e monta os links
        link = noticia.a['href'].strip()
        link = f"https://www.lanacion.com.ar{link}"
        links_list.append(link)

        # Extrai titulos
        titulo_element = noticia.h2
        titulo = titulo_element.text.strip()
        titulos_list.append(titulo)
        

def main():
    url = 'https://www.lanacion.com.ar/ultimas-noticias'

    extrair_infos(url)
    print("Links: \n", links_list, "\n \n Titulos: ", titulos_list)
    
   

if __name__ == "__main__":
    main()
