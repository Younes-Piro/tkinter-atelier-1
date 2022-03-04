from lxml import etree
from bs4 import BeautifulSoup 
  
  
with open('schema.xml', 'r') as f: 
    data = f.read() 
  
Bs_data = BeautifulSoup(data, "xml") 
  
b_unique = Bs_data.find_all('livre') 

for livre in b_unique:
    print(livre['genre'])
    print(livre.titre.text)



