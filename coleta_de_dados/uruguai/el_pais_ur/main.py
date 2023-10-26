# Importar bibliotecas
from bs4 import BeautifulSoup
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
    conteudo = html.find('main', attrs={'class': 'Page-oneColumn'})
    lista_noticia = conteudo.find_all('div', 'PromoBn')


    for noticia in lista_noticia:

        # Extrai e monta os links
        link = noticia.a['href'].strip()
        link = f"{link}"  # Nesse jornal o href já vem com o link montado
        links_list.append(link)

        # Extrai titulos
        titulo_element = noticia.text
        titulos_list.append(titulo_element) # O título desse jornal não está contido em um h2, extraindo o texto com o .text conseguimos a data e a hora junto do titulo. Mas não entendi por que ele extrai vários \n em str....

def main():
    url = 'https://www.elpais.com.uy/ultimas-noticias'

    extrair_infos(url)
    print("Links: \n", links_list, "\n Titulos: \n", titulos_list)


if __name__ == "__main__":
    main()
