from tinydb import TinyDB, Query
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import os
import re


# Listas para armazenar informações extraídas
titulo_lista = []
link_lista = []
data_lista = []
horario_lista = []
numero_da_nota_lista = []
categoria_lista = []

def extrair_infos():
    # Ao final da extração dos dados as variáveis devem ser atualizadas chamando a função da inserção e atribuindo os parâmetros necessários do json.
        inserir_bd()

# Função para criar o ambiente virtual
def criar_ambiente_virtual():
    env_dir = load_dotenv('.env_dir')
    DIR_DADOS_FINAL = os.getenv('DIR_DADOS_FINAL')
    print(DIR_DADOS_FINAL)

    # Verificar se a variável de ambiente está configurada
    if DIR_DADOS_FINAL is None:
        print("A variável de ambiente DIR_DADOS_FINAL não está configurada.")
        return
    os.makedirs(DIR_DADOS_FINAL, exist_ok=True)
    print(f"Ambiente virtual criado em {DIR_DADOS_FINAL}")
    
def inserir_bd(titulo, link, data, horario, numero_da_nota, paragrafos_lista, categorias):
    load_dotenv('.env_dir')
    DIR_DADOS_FINAL = os.getenv('DIR_DADOS_FINAL')

    # Criação ou abertura do arquivo de base de dados
    bd = TinyDB(f'{DIR_DADOS_FINAL}/coleta.json', indent=4, ensure_ascii=False)
    buscar = Query()
    verificar_bd = bd.contains(buscar.link == link)

    # Verifica se o link já está na base de dados
    if not verificar_bd:
        # Insere as informações na base de dados
        bd.insert({
            'Título': titulo,
            'Link': link,
            'Data': data,
            'Horário': horario,
            'Número da Nota': numero_da_nota,
            'Parágrafos': paragrafos_lista,            
            'Categorias': categorias

        })
        print('Informações inseridas com sucesso!')
    else:
        print('As informações já estão na base!')

def main():
    criar_ambiente_virtual()
    extrair_infos()

if __name__ == '__main__':
    main()
