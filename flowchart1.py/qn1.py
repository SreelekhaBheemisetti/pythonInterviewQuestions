# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=int(input("enter c:"))

# num = int(input("Enter the number: "))  
# list1 = [] 
# for i in range(num):  
#   list1.append([])  
#   list1[i].append(1)  
#   for j in range(1, i):  
#     list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])  
#   if(num != 0):  
#     list1[i].append(1)  
# for i in range(num):  
#   print(" " * (num - i), end = " ", sep = " ")  
#   for j in range(0, i + 1):  
#     print('{0:6}'.format(list1[i][j]), end = " ", sep = " ")  
#   print()  


#  1  2  3  4
#  12 13 14  5
#  11 16 15  6
#  10  9  8  7

# n=int(input("enter n:"))
# dir=0
# left=0
# right=n-1
# top=0
# down=n-1

# while (left<=right and top<=down):
    

n=int(input("enter n:"))
c=0
s=int(input("enter s:"))
while s<=n:
    if n%s==0:
        c+=1
    s+=1
if c==2:
    print(n,"is a prime")
elif c>2:
    print(n,"is a composite")
else:
    print(n,"is not a prime and composite")