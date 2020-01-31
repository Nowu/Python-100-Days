def tri_left(n):
    for i in range(n):
        print('*'*(i+1)+'\n')

def tri_right(n):
    for i in range(1, n+1):
        print(' '*(n-i)+'*'*i+'\n')

def tri_middle(n):
    for i in range(1, n+1):
        print(' '*(n-i)+'*'*(2*i-1)+' '*(n-i)+'\n')
tri_left(5)
tri_right(5)
tri_middle(5)