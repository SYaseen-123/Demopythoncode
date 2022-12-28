class Failed(Exception):
    pass
class Passed(Exception):
    pass

class Bank:
    def __init__(self,bank_balance):
        self.bank_balance=bank_balance
    def withdraw(self):
        print("balnce")
        self.a=int(input())
        try:
            if self.a<90:
                raise Failed
            elif self.a>self.bank_balance:
                raise Passed
        except Failed:
            print("error")

        except Passed:
            print(self.bank_balance)
        except TypeError:
            pass
obj=Bank(7990)
obj.withdraw()



