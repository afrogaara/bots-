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
    lista = list() 
    try:
        links = html.find_all("a")    
        for cada in links:
            link = cada["class"]
            lista.append(link)
        
    except Exception as error:
        print(error)
    
    return lista 


def chosse_class(lista):
    links = list() 
    for c in lista:    
        for linha in c:
            try:
                m = html.find("div", class_=linha)
                f = m.find_all("a")
            except:
                pass
            
    for cada in f:
        try:    
            link = cada['href']
            links.append(link) 
        except:
            pass
    return links 

def encontrar_telefones(link):
    for cada in link:
        try:
            columbs = soup.find_all("div", class_= cada)
            print(columbs)
        except: 
            pass

def econtrar_emails(soup):
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
            a = find_all_class(html)
            link = chosse_class(a)  
            print(link)
            encontrar_telefones(link)      
                 
        if opc == '3':
            break
            
            

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
