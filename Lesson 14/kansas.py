from random import choice
capital = "topeka"
bird = "wester guy"
flower = "sunflower"
song = "home on the range"


def randomfunfacts():
    funfacts = [
        "Kansas is a place where peoplke live",
        "som epeople like to live in kasas",
        "i cannot think of anothe thing about kansas"

    ]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfacts()
