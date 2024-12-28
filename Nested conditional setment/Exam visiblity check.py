medical_cause=input("Did you have a medical cause Y or N:")
attend=input("enter the attenedance of the student")
if medical_cause == "Y":
    print("You are allowed")
else:   
 if attend>=75:
    print ("You are allowed")    
 else:
    print("Not allowed")

