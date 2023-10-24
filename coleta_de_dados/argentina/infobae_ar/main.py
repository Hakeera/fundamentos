# Importar bibliotecas
from bs4 import BeautifulSoup
import pandas as pd
import requests


## Funções ##

def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup 


#Tentando extrair os links e os metadados das notícias através de um laço while com find_next
# Tentativa 1:

links_list = []     # Inicializa uma lista vazia para armazenar os links
titulo_list = []    # Inicializa uma lista vazia para armazenar os títulos
subtitulo_list = [] # Inicializa uma lista vazia para armazenar os subtitulos

def extrair_infos(url):
    soup = acessar_pagina(url)
    
    div = soup.find('div', class_='feed-list-wrapper')
    link = div.find('a')

    while link is not None:
        link_url = 'https://www.infobae.com' + link['href'] # Monta o link
        links_list.append(link_url)  # Adiciona o link à lista
        
        # Extrai o título 
        titulo = link.find('h2', class_="feed-list-card-headline-lean")
        titulo_list.append(titulo) # Adiciona o titulo a lista
        
        # Extrai o subtitulo
        subtitulo = link.find('div', class_='deck')
        subtitulo_list.append(subtitulo) # Adiciona o subtitulo a lista
        
        link = link.find_next('a') # Pula para o próximo link

    return links_list, titulo_list, subtitulo_list  # Retorna as listas

# O looop está pegando links do footer que também possuem a tag <a>, achei que isso não ocorreria já que a div selecionada tem como parâmetro a class_= 'feed-list-wrapper'. Quando tentei link = div.find_next para atribuir o novo link apenas de acordo com a div deu erro.



# Tentativa 2:

    #x = div.find('div', attrs = {'class':'feed-list-wrapper'})
    '''
    while True:
        x = div.find('div', class_="feed-list-wrapper")
        link = x.find('a')
        link_url = 'https://www.infobae.com' + link['href']
        print(link_url)
        link = link.find_next('a')
        
        if link == None:
            break
        
    '''
#-----------------------------------------------------------------------------------
    
# Outras atribuições que devem estar dentro do looping while.

'''
    # Extrai o título 
   
    titulo = link.find('h2', class_="feed-list-card-headline-lean feed-list-card-headline-lean-first")
    
    # Extrai o subtitulo
    subtitulo = link.find('div', class_='deck deck-first')
    
    print("Título:", titulo)
    print("Subtítulo:", subtitulo)
    print("Link:", link_url)
    print("-----------------")
'''
    
    
# De início pensei em criar o laço while dentro de main para ficar repetindo a função extrair_infos que, inicialmente, deveria pegar as informações de uma notícia, depois, ao final, atribuir um novo valor a variável que seria usada para adiquirir as próximas extrações quando a função fosse chamada novamente em main. Algo nesse formato:
'''
    def main(): 
        url = 'https://www.infobae.com/ultimas-noticias-america/'
        acessar_pagina(url):

        while link != None:
        
            extrair_infos(url)
'''
# Tentei usar, inclusive, as funções de forma separada mas estava com dificuldade de utilizar as funções find/find_all em div. Acabei optando por colocar a função acessar_pagina dentro da função extrair_infos, assim a as funções find conseguem puxar a variável div que defini logo em seguida de formar a soup.


def main(): 
    url = 'https://www.infobae.com/ultimas-noticias-america/'
    
    extrair_infos(url)
    
    print("Links:\n", links_list, "\n \nTítulos:\n", titulo_list, "\n \nSubtitulos:\n", subtitulo_list)

if __name__ == "__main__": 
    main()