n=int(input("Enter the number of elements: "))
k=int(input("Enter the range: "))
arr=[]
sum=0
for i in range (n):
    a=int(input())
    arr.append(a)
for i in range (k):
    sum=sum+arr[i]
print(sum)
      
