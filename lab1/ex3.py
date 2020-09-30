import statistics

l=[]

for i in range(3):
    a=int(input())
    l.append(a)


mult=1
for i in l:
    mult*=i

print("总和是%d"%sum(l))
print("平均值是%f"%statistics.mean(l))
print("乘积是%d"%mult)
print("最大的数字是%d"%max(l))
print("最小的数字是%d"%min(l))