import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.artsticket.com.tw/CKSCC2005/Info/Info00/Recentperformances.aspx?type=1')

soup = BeautifulSoup(r.text, 'lxml')
title = soup.select('div.program a.programTitle')
pic = soup.select('div.program img.loaded')

for i in range(len(title)):
  print(str([i]) + ' ' + title[i].text + 'https://www.artsticket.com.tw' + title[i]['href'] + '\n')

for i in range(len(pic)):
  print(str([i]) + ' ' + pic[i]['src'] + '\n')