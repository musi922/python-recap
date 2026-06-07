nationId = input("Enter your National ID: ")
detectedNumbr = nationId[5]
checkDateOfBirt = int(nationId[1:5])
print("date of birth: ", checkDateOfBirt)
if detectedNumbr == "7":
    print("This National Id ",nationId," belongs to a Female")
elif detectedNumbr == "8":
    print("This National Id ",nationId," belongs to a Male")
else:
    print("This National Id ",nationId," is Invalid")
