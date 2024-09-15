class Cat():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"hello i am a cat. I am {self.age},years old, my name is {self.name} ")
    def makesound(self):
        print("meow")
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"hello i am a dog. I am {self.age},years old, my name is {self.name} ")
    def makesound(self):
        print("bark")
cat1 = Cat("billy",3.5)
dog1 = Dog("Manchu",0.4)

for animal in (cat1,dog1):
    animal.makesound()
    animal.info()