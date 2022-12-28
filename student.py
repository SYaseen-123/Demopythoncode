class student:
    marks_bonus=1.5
    something=" "
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.somevalue=""
    @property
    def email(self):
        return'{}.{}@gmail.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return'{} {}'.format(self.first,self.last)
    def apply_bonus(self):
        self.marks=int(self.marks*self.marks_bonus)
    def something(self):
        self.somevalue=self.email
