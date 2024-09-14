class Person(object):
    def __init__(self,lname,fname):
        self.lname = lname
        self.fname = fname
    def personname(self):
        print(self.fname)
        print(self.lname)
class Student(Person):
    def __init__(self,lname,fname,year):
        super().__init__(lname,fname)
        self.year = year
x = Student("Steve","I am",2024)
x.personname()
print(x.year)
