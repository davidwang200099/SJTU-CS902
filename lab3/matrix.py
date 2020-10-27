#! /usr/bin/python3
def mul_matrix(A, B):
    """
    将矩阵A和B相乘,并且返回结果
    你可以假设传入的参数满足矩阵相乘的条件,即A的列数等于B的行数
    """
    # 在这里实现你的函数
    C=[]
    m=len(A)
    n=len(B)
    p=len(B[0])
    for i in range(m):
        C.append([])
        for j in range(p):
            C[i].append(0)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]
    return C

def print_matrix(matrix):
    """
    打印矩阵,每行的相邻元素用一个制表符('\t')隔开
    """
    # 在这里实现你的函数
    m=len(matrix)
    n=len(matrix[0])
    for i in range(m):
        for j in range(n):
            print(matrix[i][j],end='')
            if j!=n-1:
                print('\t',end='')
        print("")
                
def input_matrix(m, n):
    """
    输入一个m*n的矩阵并且返回结果
    你可以假设所有输入都是合法输入
    """
    M=[]
    for i in range(m):
        line=input().split()
        numline=[]
        for i in line:
            numline.append(int(i))
        M.append(numline)
    return M

    
def main():
    m, p, n = input().split()
    m, p, n = int(m), int(p), int(n)
    A = input_matrix(m, p)
    B = input_matrix(p, n)
    print_matrix(mul_matrix(A, B))
    
if __name__ == '__main__':
    main()
