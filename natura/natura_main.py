from bs4 import BeautifulSoup
import pandas as pd
import requests

# Criando listas para armazenar os dados
produtos_list = []
preços_list = []
categorias_list = []

## Funções ##

def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def extrair_infos(url):
    html = acessar_pagina(url)
    #div = html.find_all('div', 'natds187')
    print(html)

def main():
    url = f'https://www.natura.com.br/c/tudo-em-promocoes?page=1&pageSize=48'
    extrair_infos(url)
    
''' 
    i = 1
    while True:
        url = f'https://www.natura.com.br/c/tudo-em-promocoes?page={i}&pageSize=48'
        extrair_infos(url)
        i = i + 1
'''
if __name__ == "__main__": 
    main()
