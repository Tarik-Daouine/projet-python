import json
import requests
from bs4 import BeautifulSoup

def requestsLetudiant(url):
    dataHTML = request.get(url).text
    if len(dataHTML) < 100:
        return False
    return BeautifulSoup(dataHTML, 'lxml')

def scraping(url):
    save = []
    data = requestsLetudiant(url)

    if data == False:
        print ('request fail')
    listeEcole = data.findAll("table", {'c-pmd-table t-section-superieur'})[0].findall('tr')

    for index,ecole in enumerate(listeEcole):
        if index == 0:
            continue
        td = ecole.findAll('td')
        if len(td) == 8 :
            save.append({"id": index , 'rang': td[0].text, 'name': td[2].text,'note':td[7].text}
        
    
    with open('scraping.json','w+',encoding='utf-8') as file:
        json.dump(save,file)
        

scraping("https://www.letudiant.fr/palmares/liste-profils/palmares-des-ecoles-d-ingenieurs/palmares-general-des-ecoles-d-ingenieurs/home.html#indicateurs=900659,900660,900661,900677&criterias")



