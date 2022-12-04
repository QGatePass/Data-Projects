# Run this script twice

for r in range(1,39):
    with open(f'MatchDay{r}.csv', 'r') as f:
        u = f.readlines()
        z = []
        w = []
        p = []

    for i in range(len(u)):

        a = str(u[i])
        # Each element is a string,then append it to a list
        # Remove more useless characters
        a = a.replace('"','')
        a = a.replace("'", '')
        a = a.replace('[', '')
        a = a.replace(']', '')
        a = a.replace(',,', ',')
        a = a.replace(' ',',')
        z.append(a)

    file = f'MatchDay{r}.csv'
    with open(file, 'w') as f:
        for q in z:
            f.write(q)
    print('Done.')
print('Fiished')