a=int(input(""))
temp=a
sum=0
while(a>0):
    n=a%10
    sum=sum+n**3
    a=a//10
if(temp==sum):
        print("yes")
else:
        print("no")
      
