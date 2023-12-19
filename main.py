try:
    Age = int(input("Age: "))
    income = 20000
    risk = income/Age
    print(Age)
except ZeroDivisionError:
    print("Age can not be Zero")
except ValueError:
    print("Invalid Value")
