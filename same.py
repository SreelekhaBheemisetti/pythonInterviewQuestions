n=int(input())
a=list(map(int,input().split()))
flag=True
i=0
j=i+1
while i<len(a)-1:
    if a[i]!=a[j]:
        flag=False
        break
    i+=1
    j+=1
if flag==True:
    print("Yes")
else:
    print("No")
