a=int(input(""))
if(a>2):
    for i in range(1,1000,1):
        c=a%i  
    if(c==0):
        print('no')
    else:
        print('yes')
else:
    print('no')
    
