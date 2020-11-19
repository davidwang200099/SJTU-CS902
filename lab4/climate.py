isFirst = True
dict = {}
for row in open('climate_data_2017.csv'):

	# 跳过第一行的标题
	if isFirst:
		isFirst = False
		continue
	row=row.strip().split(',')
    if row[0]!="2017-12-25":
        continue
    if row[9] in dict:
        dict[row[9]]+=1
    else:
        dict[row[9]]=1

for i in sorted(dict.keys()):
    print("%s : %d"%(i,dict[i]))
