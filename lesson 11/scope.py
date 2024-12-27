name = "Dave"  # global scope, availabel to everything in this file
count = 1

# function has local scope


def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()
