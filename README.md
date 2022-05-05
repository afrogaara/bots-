# bots-

soup = soup.prettify() returns a string. Não pode ser usada com find_all("a"). 'str' object has no attribute 'find_all'

def find_all_links(html):
    try:
        links = html.find_all("a")        
        for link in links:
            print(link["href"]) #ao tentar adicionar cada link numa lista >list()< o valor retornado é none 
    except Exception as error:
        print(error)
    pass

#Para adicionar todos os links do site em uma lista é necessário: 
  >> def chosse_class(html):
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
>> vai pegar cada class e find_all links e adiciona-lo na lista 
