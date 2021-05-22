#Python Program to Find the Sum of Natural Numbers

n=int(input("enter a natural number till which u want the sum:"))

if n<0:
    print("the entered number is not a natural number")

else:
    i=1
    sum1=0
    while i<=n:
        sum1=sum1+i
        i=i+1

print("sum:",sum1)
