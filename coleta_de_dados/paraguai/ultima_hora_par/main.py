# Importar bibliotecas
from bs4 import BeautifulSoup
import requests


# Criando listas vazias para armazenar os dados

links_list = []
titulos_list = []
categorias_list = []
data_list = []
subtitulo_list = []

## Funções ##

def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def extrair_infos(url):
    html = acessar_pagina(url)
    conteudo = html.find('div', attrs={'class': 'Page-content'})

    lista_noticia = conteudo.find_all('div', 'PageList-items-item')

    for noticia in lista_noticia:

        # Extrai e monta os links
        link = noticia.a['href'].strip()
        link = f"{link}"
        links_list.append(link)

        # Extrai titulos
        a_tag = noticia.find('div', 'PagePromo-title')
        titulo = a_tag.a.text
        titulos_list.append(titulo)
       
        # Extrai categorias
        a_tag = noticia.find('div', 'PagePromo-category')
        categoria = a_tag.a.text
        categorias_list.append(categoria)
        
        # Extrai data
        a_tag = noticia.find('div', 'PagePromo-date')
        data = a_tag.text
        data_list.append(data)
        
        # Extrai data
        try:
            a_tag = noticia.find('div', 'PagePromo-description')
            subtitulo = a_tag.text
            subtitulo_list.append(subtitulo)
        except:
            pass
        
def main():
    url = 'https://www.ultimahora.com/ultimas-noticias'

    extrair_infos(url)

    print("Links: \n", links_list)
    print("Titulos: \n", titulos_list)
    print("Categoria: \n", categorias_list)
    print("Data: \n", data_list)
    print("Subtitulo: \n", subtitulo_list)

if __name__ == "__main__":
    main()
