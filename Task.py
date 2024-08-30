#password generator
import random
import string
import time
# function to create complex number
def password(length, complexity):
    ch=""
    if length ==0:
        print("NO PASSWORD GENERATED")
    if complexity == 1 :
        ch+=string.ascii_lowercase
    if complexity ==2 :
        ch+=string.ascii_lowercase
        ch+=string.ascii_uppercase
    if complexity ==3 :
        ch+=string.ascii_lowercase
        ch+=string.ascii_uppercase
        ch+=string.digits
        ch+=string.punctuation
    password="".join(random.choice(ch)for _ in range(length))
    return password
print(".... PASSWORD GENERATOR...")
time.sleep(0.3)
length=int(input("Enter password length:"))
if length ==0:
    print("INVALID CHOICE!")
    print("Password must contain atleast 1 character")
    print("NO PASSWORD GENERATED")
else:   
    print("...MAKE PASSWORD COMPLEX WITH COMPLEXITY LEVELS...")
    print("PRESS.....")
    time.sleep(0.3)
    print("1. For lowercase characters")
    time.sleep(0.3)
    print("2. For mixture of lower and uppercase characters")
    time.sleep(0.3)
    print("3. For mixture of lower,uppercase characters, digits and punctuations. ")
    print("*"*10)
    print("For strong password suggested is '3'")
    complexity=int(input("Please enter: "))
    if complexity not in [1,2,3]:
        print("Invalid complexity level")
        print("Hence, default complexity level will run")
        print("Your password is generated using complexity level 1")
        p=password(length,1)
        print("Password generated is : ",p)
        time.sleep(0.4)
        print()
        print("THANK YOU VISIT AGAIN")
    else:    
        p=password(length,complexity)
        print("Password generated is : ",p)
        time.sleep(0.4)
        print()
        print("THANK YOU VISIT AGAIN")
               
               


