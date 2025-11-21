#if condition only check conditio is true than exucute the staement 

#indetation mines proper spacing python is only use proper spacing 
#another language uses in courly bresas{} but python is proper spacing use this very important
#use if elif else statement 
marks = int(input("Student marks Is :"))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("student grade is ->",grade)        


#use is nesting 

age = 81

if(age >= 30):
    if( age >=80 ):
        print("you cannot Drive")   
    else:
        print("you can drive")
else:
    print("you cannot drive")