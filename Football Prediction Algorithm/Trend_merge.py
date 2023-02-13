# Import Packages
from bs4 import BeautifulSoup
import lxml
import pymysql
import os


# Change to the League directory,
# get the names of the folders,
# go back to root folder
# use the names for creating the csv files to store scraped data
with open('EligibleLeagues.csv','r')as f:
    content = f.readlines()
web = {}
for line in content:
    if line == content[0]:
        continue
    league,webname = line.split(',')
    webname = webname.replace("\n",'')
    web[league] = webname
os.chdir('Trends')
for folder,url in web.items():
    # html files already downloaded using peripheral.py
    try:
        with open(f'{str(folder)}.html','r') as f:
            soup = BeautifulSoup(f,'lxml')
        a = soup.find_all('table')
        b = soup.find_all('table',class_='sortable',id = 'btable')
        league_table = a[7].get_text()
        league_table = league_table.split("\n")
        table_text = []
        whole_text = []
        for i in league_table:
            if len(i) > 0:
                table_text.append(i)
        table_text = str(table_text)
        table_text = table_text.replace("\\xa0",'')
        table_text = table_text.replace("'',",'')
        table_text = table_text.replace("'",'')
        table_text = table_text.split(',')
        groups = int(len(table_text)/4)
        del table_text[0:3]
        q=0
        k=4
        for i in range(groups):
            whole_text.append(table_text[q:k])
            q = k
            k += 4

        # The table we want is the second one with the tag,grab the text from it and split
        last8_table =b[1].get_text()
        last8_table = last8_table.split("\n")
        doc_text = []
        j = []
        for i in last8_table:
            # Removes empty characters,and to whole text
            if len(i) > 0:
                doc_text.append(i)
        # Last row was useless,remove it
        doc_text = doc_text[:-12]
        # Find out how many teams are in league(14 is the number of columns we are scraping)
        groups = int((len(doc_text)/14))
        x=0
        y=14
        for i in range(groups):
            j.append(doc_text[x:y])
            x = y
            y += 14
        # Remove header row,because of SQL,replacing j[0] was used while i was still suffer-heading
        del j[0]
        connection =  pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='prediction',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

        # All this to conform with SQL standards😑
        table_name=str(folder)
        table_name = table_name.replace('-','')
        table_name = table_name.replace('.','')
        table_name = table_name.replace(' ','_')
        table_name = table_name+"_table"
        cur = connection.cursor()
        cur.execute(f'drop table if exists {table_name}')
        create_db = f'''CREATE TABLE {table_name}(position text,team text,games_played text,points text)'''
        cur.execute(create_db)
        named_name=str(folder)
        named_name = named_name.replace('-','')
        named_name = named_name.replace('.','')
        named_name = named_name.replace(' ','_')
        cur.execute(f'drop table if exists {named_name}')
        create_db8 = f'''CREATE TABLE {named_name}(team text,games_played text,avg_goals text,
        over_05 text,over_15 text,over_25 text,over_35 text,
        over_45 text,over_55 text,both_teams_score text,clean_sheet text,failed_to_score text,win_to_nil text,lose_to_nil text)'''
        cur.execute(create_db8)
        with connection:
            for i in whole_text:
                ap = str(i)
                ap = ap.replace('[','')
                ap = ap.replace(']','')
                ap = ap.replace(", ' ",",'")
                insert_val = f'''INSERT INTO {table_name} values({ap})'''
                cur.execute(insert_val)
                print(ap)
            for i in j:
                val = str(i)
                val = val.replace('[','')
                val = val.replace(']','')
                val = val.replace("\\xa0",'')
                val = val.replace('%','')
                insert_val = f'''INSERT INTO {named_name} values({val})'''
                cur.execute(insert_val)
                print(val)
            connection.commit()
    except:
        continue