# Importar bibliotecas
from bs4 import BeautifulSoup
import requests


# Criando listas vazias para armazenar os dados

links_list = []
titulos_list = []

'''
    A página possui divs diferentes para as primeiras 3 notícias e depois para o resto das demais 
'''



## Funções ##

def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def extrair_infos(url):
    html = acessar_pagina(url)
    conteudo = html.find('div', attrs={'class': 'Page-content'})
    
    lista_noticia = conteudo.find_all('PagePromo')
    print(lista_noticia)
    
    for noticia in lista_noticia:

        # Extrai e monta os links
        #link = noticia.link['href'].strip()
        #link = f"{link}"
        #links_list.append(link)

        '''# Extrai titulos
        titulo_element = noticia.h2
        titulo = titulo_element.text.strip()
        titulos_list.append(titulo)'''

def main():
    url = 'https://www.ultimahora.com/ultimas-noticias'

    extrair_infos(url)
    
    #print("Links: \n", links_list)
    #, "\n \n Titulos: \n", titulos_list)
   

if __name__ == "__main__":
    main()