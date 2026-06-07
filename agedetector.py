nationId = input("Enter your National ID: ")
detectedNumbr = nationId[5]
checkDateOfBirt = int(nationId[1:5])

#check you age
import time
timeNow = time.ctime()
yearNow = int(timeNow[20:24])
age = yearNow - checkDateOfBirt
print("Age: ", age)

