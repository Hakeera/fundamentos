# Importar bibliotecas
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

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
    div_noticias = html.find('div', 'col-md-8 col-lg-9')
    print(div_noticias)


def main():
        
        url = 'https://heraldodemexico.com.mx/noticias/'
        
        extrair_infos(url)

if __name__ == "__main__":
    main()
