a=0
b=1
n=int(input("Enter the number of terms to be in the series:"))
for i in range(n):
    if i==0 or i==1:
        print(i,end='\t')
    else:
        c=a+b
        print(c,end='\t')
        a=b
        b=c