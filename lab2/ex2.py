import random

totaltimes=1000000
money=0
zero=0
one=0
two=0
three=0


def rolldice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    die3 = random.randrange(1, 7)
    return (die1, die2, die3)  # pack die face values into a tuple

for i in range(totaltimes):
    dice=rolldice()
    cnt_1=dice.count(1)
    if cnt_1==1:
        one+=1
    elif cnt_1==2:
        money+=10
        two+=1
    elif cnt_1==3:
        money+=20
        three+=1
    else:
        money-=10

money=money/totaltimes
print("Player earns %f dollars on average."%money)
print("%d %d %d %d"%(zero, one,two,three))