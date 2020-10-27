def mul_matrix(A, B):
    """
    将矩阵A和B相乘,并且返回结果
    你可以假设传入的参数满足矩阵相乘的条件,即A的列数等于B的行数
    """
    # 在这里实现你的函数
    C=[]
    m=len(A)
    p=len(B[0])
    for i in range(m):
        C.append([])
        for j in range(p):
            C[i].append(0)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]

def print_matrix(matrix):
    """
    打印矩阵,每行的相邻元素用一个制表符('\t')隔开
    """
    # 在这里实现你的函数
    for i in matrix:
        for j in i:
            print(i,end='\t')
        print("\n")
                
def input_matrix(m, n):
    """
    输入一个m*n的矩阵并且返回结果
    你可以假设所有输入都是合法输入
    """
    M=[]
    for i in range(m):
        line=int(input().split())
        M.append(line)
    return M

    
def main():
    m, p, n = input().split()
    m, p, n = int(m), int(p), int(n)
    A = input_matrix(m, p)
    B = input_matrix(p, n)
    print_matrix(mul_matrix(A, B))
    
if __name__ == '__main__':
    main()
