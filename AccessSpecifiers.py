class Public_Sample_AccessModifier:
    def __init__(self,course,duration):
        self.course=course
        self.duration=duration
    def display_public_class_method(self):
        print("course:{}".format(self.course,self.duration))
publicObj=Public_Sample_AccessModifier("Python",87)
publicObj.display_public_class_method()

class Protected_Sample_Class:
    _tutor=None
    _place=None
    _experience=None
    def __init__(self,tutor,place,experience):
        self.tutor=tutor
        self.place=place
        self.experience=experience
    def _displayTutorialDetails(self):
        print("Tutor:{} -place:{} -experience:{}".format(self.tutor,self.place,self.experience))
class Derived_Protected_Class(Protected_Sample_Class):
    def display_protected_method_variables(self):
        self.displayTutorialdetails()
derivedClassObj=Derived_Protected_Class("yaseen","cerdo",8)
derivedClassObj.display_protected_method_variables()
