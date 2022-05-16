import requests 
from bs4 import BeautifulSoup # manipular html 

def cabecalho():
    header = dict()
    header['User_Agent'] = input("User-Agent: ")


def buscar_site(url, header):
   
    try:
        requisicao = requests.get(url, headers=header)
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
    lista_links = list()

    try:
        links = parsing.find_all("a")    
        for tag in links:

            print(tag["href"])
            link = tag["href"]
            
            
            if link.startswith("http"):
                lista_links.append(link)
				
		
        
        return lista_links
			
 
    except Exception as error:
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
    
def encontrar_links():
    pass
def encontrar_telefones():
    pass
def econtrar_emails():
    pass

url = input("URL: ")

crowler = set()

if __name__== "__main__":
    header = cabecalho()
    soup = buscar_site(url, header)
    if soup:
        parsing = parsing_site(soup)
        link = links_site(parsing)

        #lista = class_site(parsing)
        #encontrar_links(lista, parsing)
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
