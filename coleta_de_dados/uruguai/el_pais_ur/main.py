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

# Categorias do jornal não são bem divididas no html. A página possui categorias genéricas como "mundo/informacion/opinion" mas cada notícias pode ter outras categorias "politica/economia/judiciales/servicios".
# O jornal possui uma dinâmica de setores diferentes para cada página como o nosso globo rural. Aparentemente uma nova página como se fosse um jornal diferente para cada setor.
categorias_list = [
    "mundo",
    "opinion",
    "negocios/noticias", # Setor de negocios
    "informacion"
]

## Funções ##

def carregar_mais(url):
    # Instancia o navegador (Googl Crhome)
    service = Service()
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    
    # Scroll até o primeiro botão de carregar mais
    driver.execute_script("window.scrollBy(0, 7000000);")
    driver.execute_script("window.scrollBy(0, -300);")
    
    # Looping que aperta o botão e da scroll até apertar todos
    while True:
        try:
            time.sleep(2)
            div_botao = driver.find_element(By.CLASS_NAME, 'List-nextPage')
            botao = div_botao.find_element(By.TAG_NAME, 'a')
            botao.click()
            driver.execute_script("window.scrollBy(0, 700000);")
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, -300);")
            
        except:
            break

def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def extrair_infos(url):
    html = acessar_pagina(url)
    conteudo = html.find('main', attrs={'class': 'Page-oneColumn'})
    lista_noticia = conteudo.find_all('div', 'PromoBasic')


    for noticia in lista_noticia:

        # Extrai e monta os links
        link = noticia.a['href'].strip()
        link = f"{link}"  # Nesse jornal o href já vem com o link montado
        links_list.append(link)

        # Extrai titulos
        titulo = noticia.text
        titulos_list.append(titulo) # Não entendi por que extrai vários \n em str...

def main():

    for categoria in categorias_list:
        
        url = f'https://www.elpais.com.uy/{categoria}'
        
        carregar_mais(url)
        
        extrair_infos(url)

if __name__ == "__main__":
    main()
