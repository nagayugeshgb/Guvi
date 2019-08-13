import statistics
n=int(input(""))
arr=[]
for i in range(0,n):
    c=int(input(""))
    arr.append(c)
print(statistics.median(arr))          
