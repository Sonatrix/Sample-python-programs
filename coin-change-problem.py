'''
   coin change problem
'''

def sumCount(s,n,m):

    ''' 
       initialise table with default value of 0
    '''

    table = [0 for i in range(n+1)]

    table[0] = 1

    for i in range(0,m):
        print('start of i {}'.format(i)) 
        for j in range(s[i], n+1):
            table[j] += table[j-s[i]]
            print('**********')
            print(i,j,table[j])
            print('************')
        print('end of {}'.format(i))
    return table[n]


if __name__ == '__main__':
    s = [1,2,3]
    m = len(s)
    n = 4
    print('number of ways to make change')
    print(sumCount(s,n,m))

