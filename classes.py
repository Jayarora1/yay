class student:
    name = "Penguin"
    grade = 10
    def introduction(self):
        print("hello my name is Penguin")
    def details(self):
        print("hello my name is",self.name,"i am in grade",self.grade)

ob =student()
ob.introduction()
ob.details()