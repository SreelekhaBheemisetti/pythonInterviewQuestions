# n=int(input())
# s=input()
# i=0
# while i<n:
#     if (s[0]=="a" and s[n-1]=="b") or (s[0]=="b" and s[n-1]=="a"):
#         print("Yes")
#         break
#     elif (s[i]=="a" and s[i+1]=="b") or (s[i]=="a" and s[i-1]=="b") :
#         print("Yes")
#         break
#     elif (s[i]=="b" and s[i+1]=="a") or (s[i]=="b" and s[i-1]=="a") :
#         print("Yes")
#         break
#     else:
#         print("No")
#         break
#     i+=1

n=int(input())
s=input()
if "ab" in s or "ba" in s:
    print("Yes")
else:
    print("No")