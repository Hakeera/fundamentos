# Importar bibliotecas
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pandas as pd


# Criando listas vazias para armazenar os dados

links_list = []
titulos_list = []

## Funções ##

def next_page:
    botao = driver.find_element(By.CLASS_NAME, 'next')
    botao.click()
    
def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def extrair_infos(url):
    html = acessar_pagina(url)
    conteudo = html.find('div', attrs={'class': 'sc-6c81296d-2 csSTFm'})
    lista_noticia = conteudo.find_all('li')
    
    for noticia in lista_noticia:

        # Extrai e monta os links
        link = noticia.a['href'].strip()
        link = f"https://www.clarin.com/ultimo-momento{link}"
        links_list.append(link)

        # Extrai titulos
        titulo_element = noticia.h2
        titulo = titulo_element.text.strip()
        titulos_list.append(titulo)

def main():
    url = 'https://www.clarin.com/ultimo-momento'

    extrair_infos(url)
    
    print("Links: \n", links_list, "\n \n Titulos: \n", titulos_list)
    
    next_page

if __name__ == "__main__":
    main()