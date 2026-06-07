num = int(input("Enter a number: "))

factorial = 1

if num > 0 :
 for i in range(1,num+1):
  factorial = factorial * i
 print("The factorial of ", num, "is", factorial )

elif num == 0:
    print(1)

else:
    print("No factorial of negative number")