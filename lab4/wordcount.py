file=open("word_count.txt","r")
a=dict()

words=file.readline().split()

for word in words:
    word=word.lower()
    if word in a:
        a[word]+=1
    else:
        a[word]=1
    


for i in sorted(a.keys()):
    print("%s : %d"%(i,a[i]))
