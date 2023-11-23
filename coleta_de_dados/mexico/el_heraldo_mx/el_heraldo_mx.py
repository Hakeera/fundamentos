# Importar bibliotecas
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from urllib.parse import urlparse

# Criando listas vazias para armazenar os dados

links_list = []
titulos_list = []
subtitulos_list = []
data_list = []

## Funções ##

def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def extrair_infos(url):
    html = acessar_pagina(url)
    div_noticias = html.find('div', 'col-md-8 col-lg-9')
    artigos = div_noticias.find_all('article')
    for artigo in artigos:
        # Links
        link = artigo.a['href'].strip()
        links_list.append(link)
        # Titulos
        titulo = artigo.a['title'].strip()
        titulo_rm, titulo_limpo = titulo.split(":", 1)
        titulo_tratado = titulo_limpo.encode('latin-1').decode('utf-8')
        titulos_list.append(titulo_tratado)
        # Subtitulos
        subtitulo = artigo.find('p').text
        subtitulo_tratado = subtitulo.encode('latin-1').decode('utf-8')
        subtitulos_list.append(subtitulo_tratado)
        data_s = link.split('/')
        data = data_s[4:7]
        data_list.append(data)

def main():

    url = 'https://heraldodemexico.com.mx/mundo/'
    extrair_infos(url)
    print("Títulos:\n", titulos_list, "Links:\n", links_list, "Subtitulos:\n", subtitulos_list, "Datas:\n", data_list)
    print(data_list)
    

if __name__ == "__main__":
    main()
