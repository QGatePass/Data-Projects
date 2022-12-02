import requests  as re
from bs4 import  BeautifulSoup


page = re.get('https://www.soccerstats.com/results.asp?league=england&pmtype=round2')
soup = BeautifulSoup(page.text, 'lxml')
# soup = ofe.text
# soup = ofe.text
rows = soup.find('table',  id = 'btable').td

# print(soup)
for i in rows:
    print(i.text)

# file = 'base1.txt'
# with open(file,'w') as f:
#     for row in rows:
#         f.write(f'{row.text}\n')
# print('Done.')


