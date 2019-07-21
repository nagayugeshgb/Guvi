n=int(input(""))
q=int(input(""))
for a in range(n,q+1):
    if(a>2):
        for i in range(2,a):
            if((a%i)==0):
                break
        else:
            print(a,end=" ")
    
