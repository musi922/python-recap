import math
st=1
total=0
for st in range(2):
    marks = float(input("Enter the Marks of student : "))
    total+=marks
    average = total/2
    squareroot = math.sqrt(total)
print("Total: ", total)
print("Average: ", average)
print("Square root: ", squareroot)