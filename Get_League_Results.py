import requests  as re
from bs4 import  BeautifulSoup


web = 'https://www.soccerstats.com/results.asp?league=england_2021&pmtype=round1'
for i in range(1,39):
    # 39 because most of the leagues have 38 matchdays

    new = list(web)
    # Convert the web address to a list to be able to mutate it

    new[-1] = str(i)
    # Change the round number

    old = ''.join(new)
    # Recombine the list to a string

    # Get page HTML and parse it to bs4 for scraping

    page = re.get(str(old))
    soup = BeautifulSoup(page.text, 'lxml')
    rows = soup.find('table', id='btable')

    # Dynamically create new files for each round of fixtures
    file = f'MatchDay{i}.txt'
    with open(file, 'w') as f:
        for row in rows:
            f.write(f'{row.text}\n')
    print('Done.')
print('Finished')

for r in range(1, 39):
    with open(f'MatchDay{r}.txt', 'r') as f:
        u = f.readlines()
        z = []
        w = []
        p = []
        for i in u:
            # Remove empty lines
            j = ([i if i is not None else None])
            # This line is specific to website you use
            if j[0][0].isupper():
                w.append(j)

        w.pop(0)
        for i in range(len(w)):
            a = str(w[i])
            # Each element is a string,then append it to a list
            for j in a:
                # Remove meaninless characters(using regular expressions would be a more pythonic way to go)
                # Also Specfic to the website i used
                if j == '\\' or j == '+':
                    a = a.replace(j, '')
                    a = a.replace('xa', '')
                    a = a.replace('stats', '')
                    a = a.replace('-', ' ')
                    a = a.replace('(', ' ')
                    a = a.replace(')', ' ')
                    a = a.replace("'", '')
                    a = a.replace('[', '')
                    a = a.replace(']', '')
            a = list(a)
            a.pop(-1)

            a = ''.join(a)

            m = a.split()

            m[2] = f' \'{m[2][0:3]}\', \'{m[2][3:]}\''
            z.append(m)

    file = f'MatchDay{r}.csv'
    with open(file, 'w') as f:
        for q in z:
            f.write(f'{q}\n')
    print('Done.')
print('Fiished')

for r in range(1,39):
    with open(f'MatchDay{r}.csv', 'r') as f:
        u = f.readlines()
        z = []
        w = []
        p = []
        a = ''.join(u)

    for i in range(len(u)):
        a = str(u[i])
        # Each element is a string,then append it to a list
        for j in a:
            a = a.replace('"','')
            a = a.replace("'",'')
            a = a.replace('[','')
            a = a.replace(']', '')
            a = a.replace(',,',',')


        a = a.split()
        # Seperating the scores from the team name. Again using re would be easier.
        if len(a) == 8 and a[3][-3:-1].isnumeric():
            a[3] = f' \'{a[3][0:-3]}\', \'{a[3][-3:-1]}\''
        if len(a) == 8 and a[4][0:2].isnumeric():
            a[4] = f' \'{a[4][0:2]}\', \'{a[4][2:]}\''
        if len(a) == 9 and a[4][-3:-1].isnumeric():
            a[4] = f' \'{a[4][0:-3]}\', \'{a[4][-3:-1]}\''
        if len(a) == 9 and a[5][0:2].isnumeric():
            a[5] = f' \'{a[5][0:2]}\', \'{a[5][2:]}\''
        if len(a) == 9 and a[3][-3:-1].isnumeric():
            a[3] = f' \'{a[3][0:-3]}\', \'{a[3][-3:-1]}\''
        if len(a) == 9 and a[4][0:2].isnumeric():
            a[4] = f' \'{a[4][0:2]}\', \'{a[4][2:]}\''
        if len(a) == 10 and a[4][-3:-1].isnumeric():
            a[4] = f' \'{a[4][0:-3]}\', \'{a[4][-3:-1]}\''
        if len(a) == 10 and a[5][0:2].isnumeric():
            a[5] = f' \'{a[5][0:2]}\', \'{a[5][2:]}\''
        if len(a) == 10 and a[5][-3:-1].isnumeric():
            a[5] = f' \'{a[5][0:-3]}\', \'{a[5][-3:-1]}\''
        if len(a) == 10 and a[6][0:2].isnumeric():
            a[6] = f' \'{a[6][0:2]}\', \'{a[6][2:]}\''
        if len(a) == 10 and a[3][-3:-1].isnumeric():
            a[3] = f' \'{a[3][0:-3]}\', \'{a[3][-3:-1]}\''
        if len(a) == 10 and a[4][0:2].isnumeric():
            a[4] = f' \'{a[4][0:2]}\', \'{a[4][2:]}\''
        if len(a) == 11 and a[5][-3:-1].isnumeric():
            a[5] = f' \'{a[5][0:-3]}\', \'{a[5][-3:-1]}\''
        if len(a) == 11 and a[6][0:2].isnumeric():
            a[6] = f' \'{a[6][0:2]}\', \'{a[6][2:]}\''
        if len(a) == 11 and a[4][-3:-1].isnumeric():
            a[4] = f' \'{a[4][0:-3]}\', \'{a[4][-3:-1]}\''
        if len(a) == 11 and a[5][0:2].isnumeric():
            a[5] = f' \'{a[5][0:2]}\', \'{a[5][2:]}\''
        print(a)
        a = ''.join(a)
        z.append(a)

    file = f'MatchDay{r}.csv'
    with open(file, 'w') as f:
        for q in z:
            f.write(f'{q}\n')
    print('Done.')
    # Save to file and send to brush.py
print('Finished')