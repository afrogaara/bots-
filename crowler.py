import requests 
from bs4 import BeautifulSoup # manipular html 

def buscar_site(url):
    try:
        requisicao = requests.get(url)
        if requisicao.status_code == 200:
            return requisicao.text
        else: 
            print("Erro ao fazer requisição!")
    except Exception as error:
        print(error)    

#Parte principal 
def parsing_html(response_html):
    try:
        soup = BeautifulSoup(response_html, 'html.parser')
        soup = soup
        return soup
        #print(soup.title.get_text())
        #print(soup.title)
    except Exception as error:
        print(error)
    

#Encontra o inicio e o fechamento da tag 
#E da tag vc pega apenas os links 
def find_all_links(html):
    try:
        links = html.find_all("a")
        for link in links: 
            print(link["href"])
    except Exception as error:
        print("Link não encontrado" ,error)

def find_all_class(html):
    try:
        links = html.find_all("a")    
        for link in links:
            print(link["class"])
    except Exception as error:
        print(error)

def chosse_class(soup):
    opc = input("Digite um dos class a cima: ")
    sourcerr = soup.find("div", class_=opc)
    print(sourcerr)


url = input("URL: ")



if __name__== "__main__":
    soup = buscar_site(url)
    if soup:
        html = parsing_html(soup)
        find_all_class(html)
        chosse_class(html)        
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
