# s=input()
# i=0
# r=""
# while i<len(s)-1:
#     r=r+s[i]
#     i+=1
# r=r+"4"
# print(r)

n=int(input())
i=0
while i<=n:
    j=i
    l=0
    while j<=n-(i):
        k=i
        while k<=n-(i):
            print(i,j,k)
            k+=1
        j+=1
        l+=1
    i+=1
    j=0
    k=0
    


