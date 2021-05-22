#Python Program to Find LCM


x=int(input("first no:"))
y=int(input("second no:"))

if x>y:
    min1=x
else:
    min1=y

while(1):
    if(min1%x==0 and min1%y==0):
        print("LCM:",min1)
        break
    min1=min1+1
