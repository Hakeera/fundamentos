# Importar bibliotecas
from bs4 import BeautifulSoup
import pandas as pd
import requests


## Funções ##

def acessar_pagina(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup 


def extrair_infos(url):
    
    div = acessar_pagina(url)


#Tentando extrair os links e os metadados das notícias através de um laço while com find_next.
 
# Tentativa 1:
 
    '''
    while link != None:
        geral = div.find('div', class_="feed-list-wrapper")
        link = geral.find('a')
        link_url = 'https://www.infobae.com' + link['href']
        print(link_url)
        link = link.find_next('a')  #--> Tentei usar find_next dentro do while para "pular entre as notícias" até acabarem (none)
    '''

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

if __name__ == "__main__": 
    main()