num = int(input())
for i in range(0,num):
    for j in range(1,num-i):
        print(' ',end='')
    print((2*i+1)*'*')
for i in range(1,num):
    print(' '*i,end='')
    print((2*(num-i-1)+1)*'*')
    
