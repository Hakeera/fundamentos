# Importar bibliotecas
from bs4 import BeautifulSoup
import requests


# Criando listas vazias para armazenar os dados

links_list = []
titulos_list = []
data_list = []
categorias_list_db = []
categorias_list_site = [
    'politica',
    'pais',
    'negocios',
    'estilodevida',
    'editorial',
    'mundo',
    'investigacion',
    'lnpop'
]

def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def extrair_infos(url):
    html = acessar_pagina(url)
    divs = html.find_all('div', 'clnc ws-ln')
    for div in divs:
        # Titulos
        titulo = div.a.text
        titulos_list.append(titulo)
        # Links
        href = div.a['href']
        link = f'https://www.lanacion.com.py/category{href}'
        links_list.append(link)
        # Datas
        data = href.split('/')
        data_list.append(data[2:5])
        # Categoria
        categoria = href.split('/')
        categorias_list_db.append(categoria[1])
        
    
def main():
    
    for categoria in categorias_list_site:
        
        url = f'https://www.lanacion.com.py/category/{categoria}'
        
        extrair_infos(url)
    
    print("Titulos:\n", titulos_list, "\nLinks:\n", links_list, "\nDatas:\n", data_list, "\nCategorias:\n", categorias_list_db)


if __name__ == "__main__":
    main()
