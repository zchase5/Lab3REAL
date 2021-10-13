class Student:
  'student class definition'# optional class documentation string
  count = 0   # class variable (shared by all instances)
  
  # constructor (optional, called when instantiating a new object):
  def __init__(self, first, last, grade):
    self.first= first    # instance variables
    self.last= last
    self.grade= grade
    Student.count+=  1   # increment for each new instance
  # destructor (optional, called on deletion via 'del object'):
  def __del__(self):
    Student.count-= 1   # increment for each new instance
  # class methods:
  def displayStudent(self):
    print("Name:%s %s, Grade:%s"% (self.first, self.last, self.grade))
  
# Create objects with defined instance variables:
s1 = Student("Abbie", "Normal", 0)
s2 = Student("Sam", "Spade", 100)

# Access class methods and variables:
s1.displayStudent()
s2.displayStudent()
print("# of students = %d"% Student.count)

# Change instance variables:
s1.first = "Abby"
s1.grade = 100
s1.displayStudent()

# Delete an instance:
del s2
print("# of students after deletion = %d"% Student.count)