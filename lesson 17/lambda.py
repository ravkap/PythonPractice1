from functools import reduce
def squared(num): return num * num


print(squared(2))


def addTwo(num): return num + 2


print(addTwo(12))


def sumtotal(a, b): return a + b


print(sumtotal(4, 4))


def funcbuilder(x):
    return lambda num: num + x


addTen = funcbuilder(10)

addTwenty = funcbuilder(20)

print(addTen(7))
print(addTwenty(7))

numbers1 = (3, 7, 12, 18, 20, 21)

# squared_nums = map(lambda num:  num * num, numbers)

# print(list(squared_nums))


# odd_nums = filter(lambda num: num % 2 != 0, numbers)
# print(list(odd_nums))


numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)


print(sum(numbers, 10))


names = ["Dave", "Sara Ito", "John Jacob Jingleheimersmidth"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
