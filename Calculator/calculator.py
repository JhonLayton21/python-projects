#variables
number=int(input("Select the operation: (1: +, 2: -, 3: *, 4: /): "))
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

#addition function
def addition(a, b):
    print("result:", (a+b))

#subtraction function
def subtraction(a, b):
    print("result:", (a-b))

#multiplication function
def multiplication(a, b):
    print("result:", (a*b))

#division function
def division(a, b):
    if b != 0:
        print("result:", (a/b))
    else:
        print("Error: Division by zero is not allowed.")

#match case
match number:
  case 1:
    addition(a,b)
  case 2:
    subtraction(a,b)
  case 3:
    multiplication(a,b)  
  case 4:
    division(a,b)
  case _:
    print("Invalid operation selected.")  
