# Importar bibliotecas
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Criando listas para armazenar os dados
links_list = []
titulo_list = []
subtitulo_list = []

## Funções ##

def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def extrair_infos(url):
    html = acessar_pagina(url)
    
    div = html.find('div', 'feed-list-wrapper')
    noticias = div.find_all('a')
    
    for noticia in noticias:
        
        # Links
        href = noticia['href']
        link = f'https://www.infobae.com/{href}'
        links_list.append(link)
        
        # Títulos
        titulo = noticia.find('h2').text
        titulo_list.append(titulo)
        
        # Subtitulos
        subtitulo = noticia.find('div', 'deck deck-first')
        print(subtitulo)

def main(): 
    url = 'https://www.infobae.com/ultimas-noticias-america/'
    
    extrair_infos(url)
    
    print("Links:\n", links_list, "\n \nTítulos:\n", titulo_list, "\n \nSubtitulos:\n")
    
if __name__ == "__main__": 
    main()
