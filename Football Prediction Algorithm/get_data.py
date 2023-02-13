import requests
import lxml
from bs4 import BeautifulSoup as Bs
import pymysql

source = requests.get('https://www.soccerstats.com/leagues.asp').text
soup = Bs(source,'lxml')
with open('All leagues.csv','w') as text_file:
    for m in soup.find_all('tr',class_ = 'trow8'):
        m = m.text.split('\n')
        m = f'"({m[1]}" {m[3]} {m[4]}, {m[5]}, {m[6]}, {m[7]}, {m[8]}, {m[9]}, {m[10]}, {m[11]}, {m[12]}, {m[13]}'
        text_file.write(f"{m}\n")


connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             database = 'prediction',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

cur = connection.cursor()
drop_table = cur.execute('DROP TABLE IF EXISTS all_leagues')
create_table = f'''CREATE TABLE All_Leagues(league text,games_played text,home_wins text,\
                                            draws text,away_wins text,average_goals text,home_goals text,away_goals text,\
                                            over_15 text,over_25 text,over_35 text,bts text)'''
cur.execute(create_table)
with open('All leagues.csv','r') as text_file:
    m = text_file.readlines()
with open('All leagues.csv','w') as final_file:
    for i in m:
        i = i.replace(' ',' ,')
        i = i.replace('%','')
        i = i.replace("\\n","")
        i = i.replace('( ,','')
        i = str(i.split(sep = ','))
        i = i.replace('''['"''',"'")
        i = i.replace("\\n']","'")
        i = i.replace('"  ','')
        val = i
        print(val)
        try:
            insert_val = f'''insert into All_Leagues values({val})'''
            cur.execute(insert_val)
        except:
            continue
        final_file.write(i)
connection.commit()