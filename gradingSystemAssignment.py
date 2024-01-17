math = int(input("Enter your mark of math:"))
physics = int(input("Enter your mark of physics:"))
chemistry = int(input("Enter your mark of chemistry:"))

assert(math>=35),'You have failed because you did not consume more than or equal to 35%!'
assert(physics>=35),'You have failed because you did not consume more than or equal to 35%!'
assert(chemistry>=35),'You have failed because you did not consume more than or equal to 35%!'

precentage = ((math+physics+chemistry)/300)*100
if(precentage<=59):
    print("You got C grade")
elif(precentage<=69):
    print("You got B grade")
else:
    print("You got A grade")
