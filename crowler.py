import requests 
from bs4 import BeautifulSoup # manipular html 
import re
CORREIO = list() 

#crowler = set()
def menu():
    print("1) encontrar emails e telefones")
    print("2) encontrar links")


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
    

def find_emails(soup):
    
    try:
        emails = re.findall(r"\w[\w\. ]+\w@\w[\w\ .]+\w", soup)
         
    except:
        print("Não foi encontrado nenhum email")
    return emails
    "\w[\w\w.]+\w@\w[\w\.]+\w"
    


def fone(soup):
    
    try:
           telefone = re.findall(r"(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})", soup) 
    
    except:
        print("Não foi encontrado nenhum telefone")
    return telefone
    "(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})"
    

def saida(emails, telefone):
    for email in emails:
        if email not in CORREIO:
            print(email)
            CORREIO.append(email)
    for cel in telefone:
        for numero in cel:
            print(numero, end=" ")
        print(end="\n")
url = input("URL: ")
menu()

opc = int(input("Digite a opção escolhida: "))
if __name__== "__main__":
    header = cabecalho()
    soup = buscar_site(url, header)
    if soup:
        if opc == 1:
            emails = find_emails(soup)
            telefone = fone(soup)
            saida(emails, telefone)
        if opc == 2:
            parsing = parsing_site(soup)    
            link = links_site(parsing)
            
        
        
        #lista = class_site(parsing)
        #encontrar_links(lista, parsing)



# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://regex101.com/
#https://docs.python.org/pt-br/dev/library/re.html
#\w[\w\w.]+\w@\w[\w\.]+\w
