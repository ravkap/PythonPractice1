# String data type

# literal assignment
import math
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# # constructor function
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(first, str))

# # concatination
# fullname = first + " " + last
# print(fullname)
# fullname += "!"
# print(fullname)

# # CASTING A NUMBER TO A STRing

# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = "I like rock music from the " + decade + "s."
# print(statement)

# multiple lines
multiline = '''
Hey, How are you?                                 

I was just checking in.     

                All Good?

'''
print(multiline)

# escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("Good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                             "
print(len(multiline))
multiline = "               " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print("")


# creating a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# string index values
print(first[0])
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[0:-1])
print(first[0:])
print("")

# some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))


# boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))
print(isinstance(myvalue, str))
print("")
# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(myvalue, int))
print(isinstance(myvalue, str))
print("")

# float type

gpa = 3.28

y = float(1.14)
print(isinstance(gpa, float))
print(isinstance(gpa, str))
print("")
# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print(isinstance(comp_value, complex))
print(isinstance(comp_value, str))
print("")

# built in funtions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
print("")

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# # error if you attempt to pass incorrect data
# zip_value = int("New York")
