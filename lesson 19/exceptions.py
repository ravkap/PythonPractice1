class JustNotCoolError(Exception):
    pass


x = 2
try:
    raise JustNotCoolError("Not cool man.")
    # raise Exception("IM a custom exception.")
    # print(x/0)
    # if not type(x) is str:
    #     raise TypeError("Nah bro, strings only")
except NameError:
    print("There is a NameError. Meaning something is probably undefined.")
except ZeroDivisionError:
    print("Please dont divide by zero, Zero Division Error.")
else:
    print("No errors.")
finally:
    print("Im going to print with or w/o an error. ")
