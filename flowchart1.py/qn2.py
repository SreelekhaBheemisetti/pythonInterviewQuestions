# Construct a flowchart for obtaining the sum of a given number of terms (n) 
# for a given value of x in the following mathematical series: (Input x and n from the user)
# x-x33!+x66!-x1010!+x1515!.... upto n terxms

n=int(input("enter n:"))
x=int(input("enter x:"))
f=1
s=0
i=0
while i<=n:
    j=2*n-1
    while j>=1:
        f=f*j
        j-=1
    if i%2==0:
        s=s-(f/(x**f))
    else:
        s=s+((x**f)/f)
    i+=1
print(s)