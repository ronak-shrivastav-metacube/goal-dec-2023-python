n = int(input("Enter your number:"))
nonPrimeFlag = False
for i in range(2,n-1):
    if(n%i == 0):
        nonPrimeFlag = True
        break
if(nonPrimeFlag):
    print("Number is not prime")
else:
    print("Number is prime")
