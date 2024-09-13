# firstcalc= int(input())
# secondcalc= int(input())

def calculation(firstcalc, operation, secondcalc):
    if operation == '+':
        return(firstcalc + secondcalc)
    elif operation == '-':
        return(firstcalc - secondcalc)
    elif operation == '*':
        return(firstcalc * secondcalc)
    elif operation == '/':
        return(firstcalc/ secondcalc)
    else:
        return("Incorrect input, please try again")
    
print(calculation(1, '-', 2))
