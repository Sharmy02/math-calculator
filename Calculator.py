print("Hello, welcome to calculator!")
<<<<<<< HEAD
=======
a= int(input("Please enter your first number:"))
b= int(input("Please enter your second number:"))

calc2 = input("Select an operator +, -, /, *")

def add_ (a, b):
        
    add = a + b 
    return add

def sub_ (a, b):
        
    sub = a-b
    return sub

def div_ (a, b):
    
    divided = a/b
    return divided
       
def mult_ (a, b):
    
    divided=a*b
    return divided

if calc2 == "+":
    print(f"The sum of the equation is: {add_(a, b)}" )
elif calc2 == "-":
    print(f"The difference of the equation is: {sub_(a, b)}" )
elif calc2 == "/":
    print(f"The dividend of the equation is: {div_(a, b)}" )
elif calc2 == "*":
    print(f"The product of the equation is: {mult_(a, b)}" )

>>>>>>> 7e3007f21ad0c4765fcb516a621c5175704a1166

while True:
    a= int(input("Please enter your first number:"))
    b= int(input("Please enter your second number:"))
    calc2 = input("Select an operator +, -, /, *")
    if calc2 == "+":
        add = a+b
        print(add)
    elif calc2 =="-":
        sub = a-b
        print(sub)
    elif calc2 == "/":
        divided = a/b
        print(divided)
    elif calc2 == "*":
        multiplied=a*b
        print(multiplied)
    user = input("Do you want to continue?(y/n):")
    if user == 'y':
        continue 
    else:
        break
print("Thank you for using calculator!")
<<<<<<< HEAD

=======
>>>>>>> 7e3007f21ad0c4765fcb516a621c5175704a1166
