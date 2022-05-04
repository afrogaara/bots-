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


def parsing_html(response_html):
    try:
        soup = BeautifulSoup(response_html, 'html.parser')
        soup = soup
        return soup
        #print(soup.title.get_text())
        #print(soup.title)
    except Exception as error:
        print(error)
    

def find_all_links(html):
    links = html.find_all("a")
    for link in links: 
        print(link["href"])

url = input("URL: ")



if __name__== "__main__":
    soup = buscar_site(url)
    if soup:
        html = parsing_html(soup)
        find_all_links(html)

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
