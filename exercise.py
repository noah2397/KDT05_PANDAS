
file = 'fooddata.txt'

wholefood = []
foodC = {}
foodK = {}
foodS = {}
foodCDict = {}
key = ''

with open(file,mode='r',encoding='utf-8') as f:
    datas = f.readlines()
    flag_china=0
    for data in datas:

        if flag_china :
            print(data)
            if data[0] == 'c' :
                key = data[1:-1]
                foodC[key] = []
            else :
                foodC[key].append(data)

        if data =='endw\n' and not flag_china:
            flag_china=1 # 플래그 변수
        wholefood.append(data[:-1])




    # for data in datas:
    #     if data =='endc\n': break
    #     if data.find('c')==0:
    #         flag_china=1
    #         key = data[1:-1]
    #         print(key, type(key))
    #         foodC[key] = []
    #     else:
    #         if flag_china :
    #             foodC[key].append(data)

    for data in datas:
        if data =='endk\n': break
        if data.find('k'):
            key = data[1:-1]
            foodK[key] = []
        else:
            foodK[key].append(data)
    for data in datas:
        if data =='ends\n': break
        if data.find('s'):
            key = data[1:-1]
            foodS[key] = []
        else:
            foodS[key].append(data)
    # if
    #     for k,v in range(1,len(foodC)+1), foodC.keys():
    #         foodCDict[k] = v
print(wholefood)
print(foodC)