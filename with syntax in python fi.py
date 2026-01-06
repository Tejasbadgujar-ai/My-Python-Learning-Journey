# with syntax is build in data type and as f they also as means alise means same world but name name specking 
# and f mines like  file : they conpulsory and you write the with syntax so they have outpmatically
#close the file 

# suppoose  i just read the file using with syntax :

with open("file save data.py","r") as f:
  data = f.read()
  print(data)


# write the data using wiotrh syntax outomatically close the file:

with open("file save data.py","w")as f:
  f.write("hello today i am learning i python")

# deletein a file using module os:

# first import mpdule



# import os

# os.remove("tejas1.py") #outomatically removbe the file 



#practice questions
#create a new file "practice.txt" using python add the following data in it :
# hi everyone 
# we are leaing file i/o
# using java
# i like programing in java 

with open("practice.txt","w") as f:
  f.write("hi everyone\nwe are learning file i/o")
  f.write("\nusing java\ni like programing in java")

#2nd write a program that replace oll occurences of "java" with "python" in above file

with open("practice.txt","r")as f:
  data = f.read()
data_new = data.replace("java","python")
print(data_new) 
with open("practice.txt","w")as f:
  f.write(data_new)

#3rd seacrh in the name learning exist in file or not also i read in fuction useing the question like:

def check_for_word():
 word = "learning"

 with open("practice.txt","r") as f:
  data = f.read()
 
  if(data.find(word) != -1):
    print("found")
  else:
    print("not found")
check_for_word()

#4th                                     #39:02

#write a fuction find in which line off the file does the world "learning"  the accure first print -1 if world not found 


def check_for_line():
 word = "programing"
 data1 = True
 line_no = 1
 with open("practice.txt","r") as f :
    while data1:
      data1 = f.readline()
      if(word in data1):
         print(line_no)
         return
      line_no += 1
    return -1
     
print(check_for_line()) 


#from a file containing a numbers seprreted by comma,print the count in even number 
count = 0 
with open("practice.txt","r") as f :
  data = f.read()

  nums = data.split(",")
  for val in nums:
    if(int(val) % 2 == 0):
      count +=1
print(count)      