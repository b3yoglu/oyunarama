#Created By Beyoglu
#usepython
import requests
import os
from bs4 import BeautifulSoup
print("********STEAM OYUN ARAMA*************")
oyunun_ismi = input("Oyun ismi girin:")
r = requests.get('https://store.steampowered.com/search/?term=' + oyunun_ismi)
cikti = BeautifulSoup(r.content, 'html.parser')
cikti2 = cikti.find("div", {"class": "col search_price responsive_secondrow"})
cikti3 = cikti.find("div", {"class": "col search_released responsive_secondrow"})
cikti4 = os.linesep.join([s for s in cikti2.text.splitlines() if s])
print("Oyun Fiyatı:" + cikti4.lstrip())
print("Çıkış Tarihi:" + cikti3.text)
