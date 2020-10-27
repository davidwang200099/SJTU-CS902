n=int(input())

board=[]

for i in range(n):
    line=input()
    board.append(line)

for line in board:
    if line.count('X')==n:
        print('X')
        exit(0)
    if line.count('0')==n:
        print('0')
        exit(0)

flag=True

for j in range(n):
    ch=board[0][j]
    for i in range(n):
        if board[i][j]!=ch:
            flag=False
            break
    if flag:
        print(ch)
        exit(0)
    flag=True

ch=board[0][0]
for i in range(n):
    if board[i][i]!=ch:
        flag=False
        break
if flag:
    print(ch)
    exit(0)

flag=True
ch=board[0][-1]
for i in range(n):
    if board[i][n-1-i]!=ch:
        print('-')
        exit(0)

print(ch)
    

    