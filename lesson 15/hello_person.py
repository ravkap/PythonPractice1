def hello(name, lang):
    greetings = {
        "english": "Hello",
        "spanish": "Hola",
        "German": "Hallo"
    }
    msg = f"{greetings[lang]} {name}!!!"
    print(msg)


if __name__ == "__main__":
    import argparse

    parcer = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )

    parcer.add_argument(
        "-n", "--name", metavar="name",
        required=True, help=" the name of the perosn to greet."

    )
    parcer.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["english", "spanish", "German"],
        help="greeting language"
    )
    args = parcer.parse_args()

    hello(args.name, args.lang)
