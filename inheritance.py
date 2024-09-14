class Person( object ):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def Display(self):
        print(self.name)
        print(self.idnumber)
class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,idnumber)
    def present(self):
        print(self.salary)
        print(self.post)
a = Employee("Penguin",73829,737373,"intern")
a.Display()
a.present()
