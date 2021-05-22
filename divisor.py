#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.


list1=[]
num=int(input("enter a number:"))

for x in range((num-(num-1)),(num+1)):
    if num%x==0:
        d=num/x
        list1.append(x)

print("the divisors of this number are:",list1)

