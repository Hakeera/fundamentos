# Importar bibliotecas
from bs4 import BeautifulSoup
import requests
from tinydb import TinyDB, Query
from dataclasses import dataclass, asdict
from pathlib import Path
from dotenv import load_dotenv
import json
import os

@dataclass
class Jornal:
        jornal: str
        titulo: str
        categoria: str
        link: str
        data: str
        
        def as_dict(self):
            return asdict(self)


db_path = Path(__file__).parent/'db.json'
db = TinyDB(db_path)
db = TinyDB('db.json', indent=4, ensure_ascii=False)

# Criando listas vazias para armazenar os dados
def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def extrair_infos(url):
    jornal = "La Nacion"
    html = acessar_pagina(url)
    divs = html.find_all('div', 'clnc ws-ln')
    for div in divs:
        # Titulos
        titulo = div.a.text
        # Links
        href = div.a['href']
        link = f'https://www.lanacion.com.py/category{href}'
        # Datas
        data_p = href.split('/')
        data = data_p[2:5]
        # Categoria
        categoria_p = href.split('/')
        categoria = categoria_p[1]
        # Banco de dados
        j = Jornal(jornal, titulo, categoria, link, data)
        db.insert(j.as_dict())

def inserir_bd(titulo, link):
    env_dir = load_dotenv('.env_dir')
    DIR_DADOS_FINAL = os.getenv('DIR_DADOS_FINAL')
    criar_dir = os.makedirs(DIR_DADOS_FINAL, exist_ok= True)
    print(DIR_DADOS_FINAL)
    bd = TinyDB(f'(DIR_DADOS_FINAL)/coleta.json', indent=4, ensure_ascii=False)
    buscar = Querry()
    verificar_bd = bd.contains(buscar.link == link)
    if not verificar_bd:
        bd.insert({
            "Título": titulo,
            "Link": link
        })        

def main():
    #url = f'https://www.lanacion.com.py/category/politica'
    #extrair_infos(url)
    inserir_bd()
if __name__ == "__main__":
    main()