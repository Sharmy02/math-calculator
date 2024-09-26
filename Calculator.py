print("Hello, welcome to calculator!")

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

