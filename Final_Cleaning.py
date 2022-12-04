b =[]
for r in range(1,39):
    with open(f'MatchDay{r}.csv', 'r') as f:
        u = f.readlines()
        a = ''.join(u)

    for i in range(0,10,1):
        a = u[i].split(',')
        # Prepare the files for sql importation
        if len(a) == 10 and a[4].isnumeric():
            # If a one name team plays a one name team
            t = f"{a[0]}, {a[1]} {a[2]}, {a[3]}, {a[4][1]}, {a[5][0]}, {a[6]}, {a[7]}, {a[8]}, {a[9][0]}"
            print(t)
            b.append(t)
        elif len(a) == 11 and a[5].isnumeric() and a[6].isnumeric():
            # if a two name team plays a one name team
            t = f"{a[0]}, {a[1]} {a[2]}, {a[3]} {a[4]}, {a[5][1]}, {a[6][0]}, {a[7]}, {a[8]}, {a[9]}, {a[10][0]}"
            print(t)
            b.append(t)
        elif len(a) == 11 and a[4].isnumeric() and a[5].isnumeric():
            # if a one name team plays a two name team
            t = f"{a[0]}, {a[1]} {a[2]}, {a[3]}, {a[4][1]}, {a[5][0]}, {a[6]} {a[7]}, {a[8]}, {a[9]}, {a[10][0]}"
            print(t)
            b.append(t)
        elif len(a) == 12 and a[5].isnumeric() and a[6].isnumeric():
            # If a two name team plays a two name team
            t = f"{a[0]}, {a[1]} {a[2]}, {a[3]} {a[4]}, {a[5][1]}, {a[6][0]}, {a[7]} {a[8]}, {a[9]}, {a[10]}, {a[11][0]}"
            print(t)
            b.append(t)
        elif len(a) == 12 and a[6].isnumeric() and a[7].isnumeric():
            # If a three name team plays a one name team
            t = f"{a[0]}, {a[1]} {a[2]}, {a[3]} {a[4]} {a[5]}, {a[6][1]}, {a[7][0]}, {a[8]}, {a[9]}, {a[10]}, {a[11][0]}"
            print(t)
            b.append(t)
        elif len(a) == 12 and a[4].isnumeric() and a[5].isnumeric():
            # If a one name team plays a three name team
            t = f"{a[0]}, {a[1]} {a[2]}, {a[3]}, {a[4][1]}, {a[5][0]}, {a[6]} {a[7]} {a[8]}, {a[9]}, {a[10]}, {a[11][0]}"
            print(t)
            b.append(t)
        elif len(a) == 13 and a[6].isnumeric() and a[7].isnumeric():
            # If a three name team plays a two name team
            t = f"{a[0]}, {a[1]} {a[2]}, {a[3]} {a[4]} {a[5]}, {a[6][1]}, {a[7][0]}, {a[8]} {a[9]}, {a[10]}, {a[11]}, {a[12][0]}"
            print(t)
            b.append(t)
        elif len(a) == 13 and a[5].isnumeric() and a[6].isnumeric():
            # If a two name team plays a three name team
            t = f"{a[0]}, {a[1]} {a[2]}, {a[3]} {a[4]}, {a[5][1]}, {a[6][0]}, {a[7]} {a[8]} {a[9]}, {a[10]}, {a[11]}, {a[12][0]}"
            print(t)
            b.append(t)
print('\n')
for i in b:
    print(i)

with open('epl_2021.csv', 'w') as f:
# Combine all fixtures in one file and send to Sql/Excel/Pandas
    for x in b:
        f.write(f'{x}\n')
        print('done')
