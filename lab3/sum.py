a=input()
if len(a)==0:
    print("0.000000")
    exit(0)
sum=0.0

a=a.split(',')

if len(a)!=0:
    for i in a:
        sum+=float(i)

print("%.6f"%sum)