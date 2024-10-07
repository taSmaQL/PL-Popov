# 8 Попытка
from bs4 import BeautifulSoup
import requests
import time
import re
import json
HOST = 'https://vsuet.ru'
URL = 'https://vsuet.ru/obuchenie/faculties'

HEADERS = {
      'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

def analize_website(URL,HEADERS):
    res = requests.get(URL,headers=HEADERS)
    soup = BeautifulSoup(res.text,'lxml')
    return soup

# soup = analize_website(URL,HEADERS)
# four_faculties = soup.find_all('a',class_='box-service__item')
# all_details_of_faculties = {}
# for item in four_faculties:
#       item_text = item.text
#       item_hrefs = HOST + item['href']
#       all_details_of_faculties[item_text] = item_hrefs

def create_json(x,xx):
      with open(xx,'w',encoding='utf-8') as file:
            json.dump(x,file,indent=4,ensure_ascii=False)
      return file

def add_json(x,xx):
      with open(xx,'a',encoding='utf-8') as file:
            json.dump(x,file,indent=4,ensure_ascii=False)
      return file

# jsonfirst = create_json(all_details_of_faculties,'Name_name.json')

with open('Name_name.json',encoding='utf-8') as file:
      y = json.load(file)

      for name_faculties,href_faculties in y.items():
            try:
                  soup = analize_website(href_faculties,HEADERS)
                  dekan = soup.find('div',class_='dept-info__h-name').text
                  contancts = soup.find_all('span',class_='line-contacts')
                  number = contancts[0].text
                  email = contancts[1].text
                  address = contancts[2].text
                #   block = soup.find('div',class_='col-lg-3 pr-lg-2 pl-lg-0')
                #   N_kafedra = block.find_all('a',text=re.compile('Кафедра'))
                #   all_details_of_kafedra = {}
                #   for x in N_kafedra:
                #         x_text = x.text
                #         x_hrefs = HOST + x['href']
                #         all_details_of_kafedra[x_text] = x_hrefs
                        # time.sleep(1)
                #   jsonsecond = add_json(all_details_of_kafedra,'Name_name_name.json')
            except Exception as ex:
                  print(ex)
            
with open('Name_name_name.json',encoding='utf-8') as file:
      z = json.load(file)
      
      for name_kafedra,href_kafedra in z.items():
            try:
                  soup = analize_website(href_kafedra,HEADERS)
                  zav_dekan = soup.find('div',class_='dept-info__h-name').text
            except Exception as ex:
                  print(ex)

      for name_kafedra,href_kafedra in z.items():
            try:
                  soup = analize_website(href_kafedra + '/sotr',HEADERS)
                  block = soup.find('div',class_='article')
                  name_sotr = block.find_all('a',class_='person-name')
                  for teacher in name_sotr:
                        teacher_text = teacher.text
            except Exception as ex:
                  print(ex)
