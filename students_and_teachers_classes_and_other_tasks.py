class person():

  def __init__(self,name,age,subjects):
    self.name = name
    self.age = age
    self.subjects = subjects

  def human_call(self):
    print("I talk.")


class student(person):

  def __init__(self,person,class_group,activities,grades):
    person.__init__(self,class_group)
    self.class_group = class_group
    person.__init__(self,activities)
    self.activities = activities
    person.__init__(self,grades)
    self.grades = grades

  def student_call(self):
    print("Sheeesh.")


class teacher(person):

  def __init__(self,person,overtime,qualifications):
    person.__init__(self,overtime)
    self.overtime = overtime
    person.__init__(self,qualifications) 
    self.qualifications = qualifications

  def teacher_call(self):
    print("FML.")

student_1 = student("1","Class_1","Swim",["A", "B", "A", "D"])
student_1.name = "Manny"
student_1.age = "50"
student_1.subjects = ["Cross-fit", "Cross-stitch", "Cross-country","Hot Cross Bun"]
print(vars(student_1))
student_1.student_call()


#multiple inheritance testing
class student_teacher(student,teacher):

  def __init__(self,subjects):
    self.subjects = subjects

    

#task A3
#can you print all numbers from 1 to 10 using range
#can you print all numbers between 1:100 using range with increase of 4

for i in range(10):
  print(i)

for i in range(100):
  if i%4 == 1:
    print(i)

#task A4 - FizzBuzz game
#Program should print each number from 1 to 100
#if number is divisible by 3 it should intead print fizz
#if number is divisible by 5 it should print buzz
#if number is divisible by both 3 and 5, it should print FizzBuzz

for i in range(100):
  if i%3 == 0 and i%5 == 0:
    print("FizzBuzz")
  elif i%3 == 0:
    print("Fizz")
  elif i%5 == 0:
    print("Buzz")
  else:
    print(i)

#task A5 - Emoji repeater
#Create one using for loop
#Create one using while loop
#Can you create one without using any loops?

for i in range(10):
  asdf = "\U00001f600" *i
  print(asdf)

i = 1
while i in range(10):
  asdf = "\U00001f600" *i
  print(asdf)
  i += 1

#doing without for loops:
print("""
"\U00001f600"
"\U00001f600\U00001f600"
"\U00001f600\U00001f600\U00001f600"
"\U00001f600\U00001f600\U00001f600\U00001f600"
"\U00001f600\U00001f600\U00001f600\U00001f600"
""")

#for tasks A6 and A7, see attached link