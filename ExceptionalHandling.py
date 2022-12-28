def divi():
     try:
        a=int(input())
        b=int(input())
        return a/b
     except ZeroDivisionError:
        print("Denominator is Zero")
     except ValueError:
        print("yaseen")
print(divi())