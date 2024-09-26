# n,l=map(int,input().split())
# a=list(map(int,input().split()))
# i=0
# c=0
# while i<n:
#     if a[i]>=l:
#         c+=1
#     i+=1
# print(c)

n,l,r=map(int,input().split())
a=list(map(int,input().split()))
i=0
while l<=r:
    per=abs(l-a[i])
    l+=1
