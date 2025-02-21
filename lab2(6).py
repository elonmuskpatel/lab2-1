x=int(input("enter a number:"))
c=0
while x!=0:
    x//=10
    c+=1
print("number of digits:",c)
