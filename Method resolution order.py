#Daimond Problem
class HigherParentClass:
    def print_something(self):
        print("this  is from higher parent class")
class LowerParentClass1(HigherParentClass):
    def print_something(self):
        print("this is from lower parent class1")
class LowerParentClass2(HigherParentClass):
    def print_something(self):
        print("this is from lower parent class2")
class ChildClass(LowerParentClass1,LowerParentClass2):
    def print_something(self):
        HigherParentClass.print_something(self)
childClassObj=ChildClass()
childClassObj.print_something()
