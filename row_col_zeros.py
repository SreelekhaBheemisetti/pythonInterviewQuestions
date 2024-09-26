# rows=int(input("Enter rows:"))
# cols=int(input("Enter cols:"))
# matrix=[]
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         val=int(input("Enter value:"))
#         row.append(val)
#     matrix.append(row)
# print(matrix)

a=[[1,2,4],[3,0,1],[2,1,1]]
l=[]
te=a
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]==0:
            c=[i][j]
            l.append(c)
print(l)
# for i in range(len(te)):
#     for j in range(len(te[i])):
#         if j==l[j]
