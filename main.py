setka = {}
n = int(input())
for i in range(n):
    match = input().split(';')
    if match[0] not in setka.keys():
        setka[match[0]]=[0,0,0,0,0]
    if match[2] not in setka.keys():
        setka[match[2]]=[0,0,0,0,0]
    if int(match[1]) > int(match[3]):
        setka[match[0]][0] += 1
        setka[match[0]][1] += 1
        setka[match[0]][4] += 3
        setka[match[2]][0] += 1
        setka[match[2]][3] += 1
    elif int(match[1]) < int(match[3]):
        setka[match[2]][0] += 1
        setka[match[2]][1] += 1
        setka[match[2]][4] += 3
        setka[match[0]][0] += 1
        setka[match[0]][3] += 1
    else:
        setka[match[0]][0] += 1
        setka[match[0]][2] += 1
        setka[match[0]][4] += 1
        setka[match[2]][0] += 1
        setka[match[2]][2] += 1
        setka[match[2]][4] += 1    
for team in setka:
    score = setka.get(team)
    print('{}:{} {} {} {} {}'.format(team, score[0], score[1], score[2], score[3], score[4]  ))
