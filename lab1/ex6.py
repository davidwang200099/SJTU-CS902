def fibonacci_recur(i):
    '''
        Calculating f(i) recursively
    '''
    if i==1 or i==2:
        return 1
    return fibonacci_recur(i-1)+fibonacci_recur(i-2)

def fibonacci_iter(i):
    '''
       Calculating f(i) iteratively
    '''
    p=1
    q=1
    j=1
    while j!=i and j!=i-1:
        p=p+q
        q=q+p
        j+=2
    if i%2==0:
        return q
    else:
        return p

def main():
    for i in range(10):
        print(fibonacci_iter(i+1))

if __name__ == '__main__':
    main()