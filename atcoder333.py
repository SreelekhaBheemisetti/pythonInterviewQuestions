# n=int(input())
# print(str(n)*n)
# A=1
# C=1
# E=1
# B=0
# D=0
# s=input()
# t=input()
# # a=["A":1,"B":2,"C":1,"D":2,"E":1]
# if s[0]*s[1]==t[0]*t[1]:
#     print("Yes")
# else:
#     print("No")

s=input()
t=input()
l=["AC","AD","BD","BE","CA","CE","DA","DB","EB","EC"]
l1=["AB","BC","CD","DE","EA","BA","CB","DC","ED","AE"]
if ((s in l) and (t in l)) or ((s in l1) and (t in l1)):
    print("Yes")
else:
    print("No")