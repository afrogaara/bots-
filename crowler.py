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
 
def parsing_site(response_html):
    try:
        soup = BeautifulSoup(response_html, 'html.parser')
        parsing = soup
        return parsing
        #print(soup.title.get_text())
        #print(soup.title)
    except Exception as error:
        print(error)
    

#Encontra o inicio e o fechamento da tag 
#E da tag vc pega apenas os links 

def links_site(parsing):
    try:
        links = parsing.find_all("a")    
        for link in links:
            print(link["href"])
    except Exception as error:
        print(error)
    pass

def class_site(parsing):
    lista = list() 
    try:
        links = parsing.find_all("a")    
        for cada in links:
            link = cada["class"]
            lista.append(link)
    except:
        pass
    return lista 
    
def encontrar_links(lista, parsing):
    href = list()
    for links in lista:
        for link in links:
            print(link, end="  ")
    print("\n")
    opc = input(": ")    
    try:
        m = parsing.find('div', class_=opc)
        f = m.find_all("a")
        print(f)
    except:
        print("não foi encontrado")
    for cada in f:
        try:    
            link = cada['href']
            href.append(cada) 
            print(cada)
        except:
            pass
    

def encontrar_telefones(link):
    for cada in link:
        try:
            columbs = soup.find_all("div", class_= cada)
            print(columbs)
        except: 
            print("nada encontrado!")

def econtrar_emails(soup):
    pass


url = input("URL: ")


if __name__== "__main__":
    soup = buscar_site(url)
    if soup:
        parsing = parsing_site(soup)
        #links_site(parsing) ok 
        lista = class_site(parsing)
        encontrar_links(lista, parsing)
        
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

