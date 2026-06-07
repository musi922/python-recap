#block of codes that work together to perfom specific task
#types of function(User-defined Function and Builtin Function)

### user defined function.

#def functionName()  #fn Declaration
#return Value  #statement
#print(functionName()) #fn call

def Calculator(num1,num2,operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Invalid Operator")

Calculator(num1=12,num2=3,operator="+")