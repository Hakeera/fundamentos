# Importar bibliotecas
from bs4 import BeautifulSoup
import requests


'''
    - Os links do jornal la nacion contém todos os metadados necessários: categoria (incluindo uma subcategoria),o titulo da notícia e a data no formato(dd/mm/aaaa)
    - Links das notícias encontrados na div: <div class="breaking-news"> == 0$
    - Cada notícia tem seus dados dentro de cada div <article class="mod-article" data-section="CuerpoAcu" data-event="LinkClick">. Esse div é subdivido em uma div para o horário, uma div para a foto (NESSA DIV QUE TEMOS O LINK) e uma div para a descrição(com o h2 que contém PARTE do titulo da notícia) 
    - Div do botão/foto (LINK): <div class="content-media">, <section role= "button", class="mod-media ">, <figure role="button" class= "mod figure -- horizontal">, <a href]
    - Div do título(h2): <section class="mod-description">  ESSA DIV TAMBÉM CONTEM O LINK!! (<a href="LINK" class="com-link">TÍTULO</a>)
'''

## Funções ##

# Criando listas vazias para armazenar os dados

links = []
titulos = []

# Extrair data

for link in links:
    
    parts = link.split('/')
    data = parts[-1]
    print(data)


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
        links.append(link)

        # Extrai titulos
        titulo_element = noticia.h2
        titulo = titulo_element.text.strip()
        titulos.append(titulo)


def main():
    url = 'https://www.lanacion.com.ar/ultimas-noticias'

    extrair_infos(url)



if __name__ == "__main__":
    main()
