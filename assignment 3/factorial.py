num=int(input("Enter a number : "))
fac=1
for i in range(1,num+1):
    fac=fac*i
print(f"factorial of {num} is {fac}")

def fact(num):
    if(num==1 or num==0):
        return 1
    else:
        return num*fact(num-1)

fac=fact(num)
print(f"factorial of {num} is {fac}")