import math
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b!=0:
        return a/b
    else:
        return "ERROR! Zero division error"
def log(n,base):
    return math.log(n,base)
def sq(n):
    return n**2
def qu(n):
    return n**3
def pw(x,y):
    return math.pow(x,y)
def sqt(x):
    return x**0.5
def calculator():
    while True:
        
        print("Select operation to do ")
        print("1. ADDITION")
        print("2. SUBTRACTION")
        print("3. MULTIPLICACTION")
        print("4. DIVISION")
        print("5. SQUARE OF  NUMBER")
        print("6. CUBE OF A NUMBER")
        print("7. LOG OF A NUMBER ")
        print("8. SQUARE ROOT OF A NUMBER")
        print("9. POWER OF X ^Y")
        print("10. EXIT")
        choice=int(input("PRESS THE NUMBER :"))

        if choice in [1,2,3,4,7,9]:
            num1=float(input("PRESS NUMBER 1 : "))
            num2=float(input("PRESS NUMBER 2 : "))
            if choice ==1:
                
                a=add(num1,num2)
                print(f"SUM OF {num1} AND {num2} IS {a} .")

            elif choice==2:
                
                s=sub(num1,num2)
                print(f"SUBTRACTION OF {num1} AND {num2} IS {s} .")
            elif choice==3:
                
                m=multiply(num1,num2)
                print(f"MULTIPLICATION OF {num1} AND {num2} IS {m}")
            elif choice==4:
                
                d=division(num1,num2)
                print(f"DIVISION OF {num1} AND  {num2} IS {d} .")
            
            elif choice==7:
                print(f"TAKING {num1} AS NUMBER AND {num2} AS BASE .")
                l=log(num1,num2)
                print(f"LOG OF {num1} WITH {num2} AS BASE IS {l} .")
            elif choice==9:
                print(f"CONSIDERING {num1} AS BASE AND {num2} AS EXPONENT .")
                r=pw(num1,num2)
                print(f"{num1} TO THE POWER{num2} IS {r} . ")
        elif choice in [5,6,8]:
            num=float(input("ENTER NUMBER : "))
            if choice==6:
                
                s=qu(num)
                print(f"CUBE OF {num} IS {s} .")
            elif choice==5:
                
                s=sq(num)
                print("SQUARE OF ",num, "IS",s,".")
            elif choice==8:
                
                qrt=sqt(num)
                print(f"SQUARE ROOT OF {num} IS {qrt} .")
        
        elif choice== 10:
            break
        else:
            print("INVALID CHOICE")
            print("PLEASE ENTER CORRECT OPTION ")
            continue
# 1 2 3 4 7 9
        while True:
            next=input("DO YOU WANT TO SOLVE ANOTHER QUESTION: (yes/no)   :  ").strip().lower()
            if next not in ['yes','no']:
                print("Invalid choice")
                continue
            elif next =="yes":
                break
            
            else:
                break

        if next=='no':
            print("Thank you")
            break
print(".....Welcome to basic calculator.....")
print("*"*40)
calculator()

