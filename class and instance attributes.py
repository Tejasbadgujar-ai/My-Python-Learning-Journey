#class.attr
#objects.attr

class Students():
    college_name = "ssbt college"  #class attribut repeated time same name mentioned him class attributes
    #like suppose lot off peapeples learning in same school so this school name repeated so this mentioned in class beacuse they only one time 
    #than can outomaticalkly repeated 
    name = "anonymous"  #class attribute same name 

    def __init__(self,name,marks):
      self.name=name #objects attribute same name everytime object are executed
      self.marks=marks # because object>class attributes everytime not same in class and objects attributes every time different only this time prefered then 
      print("adding new student in database")

s1 = Students("tejas",96)   
print(s1.name,s1.marks)

s2 = Students("badgujar",97)
print(s2.name,s2.marks)

print(s1.college_name,s2.college_name)

s1 =Students("arjun",42)
print(s1.name)