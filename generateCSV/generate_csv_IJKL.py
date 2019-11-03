from pymongo import MongoClient
import csv


clint = MongoClient()
db = clint['testMapList']

# items = db.mapingCollection.find({'startline1':11,'endline1':16})
items = db.mapingCollection.find()
cnt = 0
num = 0
file = open('mongoInfo_IJKL.csv','w')
writer = csv.writer(file)

array = []
for item in items:
    project_name = item['path'][:item['path'].find('/')]
    # print(project_name)
    init = item['path'][:1].upper()
    ppath_mongo = item['path'].replace('/','\\')
    tpath_mongo = item['testpath'].replace('/','\\')

    if init == 'I' or init == 'J' or init == 'K' or init == 'L':
        ppath = 'D:\\ryosuke-ku\\data_set\\Git_20161108\\IJKL\\' + ppath_mongo
        tpath = 'D:\\ryosuke-ku\\data_set\\Git_20161108\\IJKL\\' + tpath_mongo
        # writer.writerow([project_name, ppath, tpath])
        array.append(project_name + ',' + tpath + ',' + ppath)

    else:
        num += 1
    cnt += 1
print(cnt)
print(num)

cleanArray = list(set(array))
print(cleanArray)
reigai = 0
for info in cleanArray:
    infoArray = info.split(',')
    print(infoArray)
    print(len(infoArray))
    if len(infoArray) != 3:
        reigai += 1
    else:
        writer.writerow(infoArray)


print('reigai : ' + str(reigai))
print('detect projects' + str(len(cleanArray)))