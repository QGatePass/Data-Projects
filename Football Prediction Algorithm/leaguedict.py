import os,requests

with open('EligibleLeagues.csv','r')as f:
	content = f.readlines()
web = {}
for line in content:
	if line = content[0]:
		continue
    a,b = line.split(',')
    b = b.replace("\n",'')
    web[a] = b
os.chdir('Trends')
for i,j in web.items():
	try:
		url = requests.get(f'https://www.soccerstats.com/trends.asp?league={j}').text
		with open(f'{i}.html','w') as f:
		    f.write(url)
		print(f'{i}:  {j}')
	except:
		continue
print('done')
