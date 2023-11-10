# Importar bibliotecas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests


## Funções ##

# Criando listas vazias para armazenar os dados

links_list = []
titulos_list = []
url = [
    "economia", # - Botão de carregar mais para de funcionar
    "el-mundo",
    "sociedad",
    "el-mundo",
    
]

def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def carregar_pagina(url):
    # Instanciar navegador
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    # Loop que clica no botão de carregar mais
    while True:
        try:
            driver.execute_script("window.scrollBy(0, 700000);")
            driver.execute_script("window.scrollBy(0, -300);")
            time.sleep(2)
            botao = driver.find_element(By.XPATH, '//button[@title="Ver más notas de SOCIEDAD"]')
            botao.click()

        except:
            break
    
def extrair_infos(url):
    html = acessar_pagina(url)
    conteudo = html.find('div', attrs={'class': 'breaking-news'})
    lista_noticia = conteudo.find_all('article')

    for noticia in lista_noticia:

        # Extrai e monta os links
        link = noticia.a['href'].strip()
        link = f"https://www.lanacion.com.ar{link}"
        links_list.append(link)

        # Extrai titulos
        titulo_element = noticia.h2
        titulo = titulo_element.text.strip()
        titulos_list.append(titulo)
        

def main():
    url = 'https://www.lanacion.com.ar/ultimas-noticias'

    extrair_infos(url)
    carregar_pagina(url)
    
    print("Links: \n", links_list, "\n \n Titulos: ", titulos_list)
    
   

if __name__ == "__main__":
    main()
