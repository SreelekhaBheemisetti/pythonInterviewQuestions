# n=int(input())
# s=input()
# i=0
# ind=0
# while i<n-2:
#     if s[i]=="A" and s[i+1]=="B" and s[i+2]=="C":
#         ind=i+1
#         break
#     i+=1
# if ind>0:
#     print(ind)
# else:
#     print("-1")


n,m=map(int,input().split())
s=input()
t=input()
if (s[0]==t[0] and s[n-1]==t[n-1]) and (s[-1]==t[-1] and s[-n]==t[-n] and s[-n-1]==t[-n-1]):
    print("0")
elif s[0]==t[0] and s[n-1]==t[n-1]:
    print("1")
elif s[-1]==t[-1] and s[-n]==t[-n] and s[-n-1]==t[-n-1]:
    print("2")
else:
    print("3")
