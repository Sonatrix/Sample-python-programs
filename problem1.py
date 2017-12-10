n,m,k = [int(i) for i in raw_input().split(' ')]
a = [int(i) for i in raw_input().split(' ')]
array = []
for i in range(m):
    ar = []
    for j in range(k):
        ar.append(0)
    array.append(ar)
student = 0
for i in a:
    if array[i].count(1) < k:
        array[i][array[i].index(0)] = 1
    elif array[i].count(1) == k:
        student = student + 1

print('hello')
print(student)
