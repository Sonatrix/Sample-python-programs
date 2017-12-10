num = 5
#print("+", "-"*4, "+", "-"*4, "+")
def bottomLine(num): 
    print("|",end=" ")
    print(" "*num,end=" ")
    print("|",end=" ")
    print(" "*num,end=" ")
    print("|")

def horizontalLine(num):  
    print("+",end=" ")
    print("-"*num,end=" ")
    print("+",end=" ")
    print("-"*num,end=" ")
    print("+")
horizontalLine(num+1)
for i in range(num+1):  
    bottomLine(num+1)
horizontalLine(num+1)
for i in range(num+1):  
    bottomLine(num+1)
horizontalLine(num+1)



