from datetime import datetime
a=input("")
b=input("")
format='%H:%M'
time=datetime.strptime(a,format)-datetime.strptime(b,format)
print(time)
