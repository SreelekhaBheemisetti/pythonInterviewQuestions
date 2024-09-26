# vector<int> Solution::spiralOrder(const vector<vector<int> > &A) {
    
# T=0
# B=A.size()-1;
# L=0;
# R=A[0].size()-1;
# dir=0;
# int i;
# vector<int> ans

# while(T<=B and L<=R):
#     if(dir==0):
#         for(i=L,i<=R,i+=1)
#             ans.push_back(A[T][i])
#         T+=1
#     else if(dir==1)
#         for(i=T,i<=B,i+=1)
#             ans.push_back(A[i][R])
#         R-=1
#     else if(dir==2):
#         for(i=R,i>=L,i-=1)
#             ans.push_back(A[B][i])
#         B-=1
#     else if(dir==3):
#         for(i=B,i>=T,i-=1)
#             ans.push_back(A[i][L])
#         L+=1
#     dir=(dir+1)%4
# return ans
# dir=0
# n=int(input())
# top=0
# right=n-1
# left=0
# down=n-1
# while (top<=down and left<=right):
#     if(dir==0):
#         for ()