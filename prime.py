n=int(input("enter the number"))
i=2
flag=1
while i<=(n/2):
    if n%i==0:
         flag=0
    i=i+1
if flag==1:
    print("prime")
else:
    print("not prime")