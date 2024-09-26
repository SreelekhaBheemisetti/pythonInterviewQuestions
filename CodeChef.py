# for t in range(int(input())):
#     a,b=map(int,input().split()


# s=input()
# l=[]
# o=[]
# i=0
# while i<len(s):
#     o.append(s[i])
#     if s[i]=="|":
#         l.append(i)
#     i+=1
# del o[l[0]:l[1]+1]
# j=0
# while j<len(o):
#     print(o[j],end="")
#     j+=1

# 3
# 2
# 1
# 0
l=[]
n=100
for i in range(n):
    a=int(input())
    if a!=int:
        break
    else:
        l.append(a)
print(l)