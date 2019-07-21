n=int(input(""))
q=int(input(""))
for i in range(n+1,q,1):
    temp=i
    sum=0
    while(temp>0):
        a=temp%10    
        sum=sum+a**3
        temp=temp//10
    if(i==sum):
        print(i)
      
