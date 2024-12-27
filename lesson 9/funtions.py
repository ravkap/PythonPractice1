def hello_world():
    print("Hello World!")


# have to call the funtion
hello_world()
# cxreate simple funtion that follows parameters, parameter doesnt change, arghument changes

# defayult parameter values in case no input num2=0


def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        print("Numebers are required. Enter two numbers.")
        return
    return num1 + num2


total = sum(5, 8, 10)
print(total)
total = sum("A", "b")
print(total)


# when usiong unknown number of variables use an asterisk(*) first to make the
# type a tuple


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sarah")
multiple_items(1, 2, 3)


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="John")
