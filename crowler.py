import requests 
from bs4 import BeautifulSoup # manipular html 


def menu(url):
    print(f"1) encontrar links do {url}")
    print(f"2) encontrar class do {url}")
    print("3) para sair.")
    pass


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
        print(error)
    pass

def find_all_class(html):
    try:
        links = html.find_all("a")    
        for link in links:
            print(link["class"])
    except Exception as error:
        print(error)

def chosse_class(html):
    links = list() 
    opc = input("Digite um dos class a cima: ")
    try:
        m = html.find("div", class_=opc)
        f = m.find_all("a")
        for cada in f:
            link = cada['href']
            links.append(link)
        return links 
    except:
        print("não encontrado!")

def encontrar_telefones():
    pass


def econtrar_emails():
    pass


url = input("URL: ")


if __name__== "__main__":
    soup = buscar_site(url)
    if soup:
        html = parsing_html(soup)
    while True:
        menu(url)
        opc = input(": ")[0]
        if opc == '1':
            find_all_links(html)
        
        if opc == '2':   
            find_all_class(html)
            link = chosse_class(html)        
            print(link)
        
        if opc == '3':
            break
            
            

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
