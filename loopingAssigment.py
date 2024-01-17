number = int(input("Enter an integer number:"))
for i in range(1,number+1):
    if(i%10==0):
        continue
    print(i)