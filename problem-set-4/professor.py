import random


def main():
    level = get_level()
    i = 0
    while i < 10:
        a, b = generate_integer(level)
        sum = input(f"{a} + {b} = ")
        if a + b == int(sum):
            print(f"in the first loop, i is {i}")
            i += 1
            continue
        else:
            print("EEE")
            for j in range(3):
                if a + b == int(sum):
                    break
                else:
                    sum = input((f"{a} + {b} = "))
                    print("EEE")
                    j = +1
                    continue
            print(f"{a} + {b} = {a+b}")
            i+= 1


def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit and int(level) in [1, 2, 3]:
            return level
        else:
            continue


def generate_integer(level):
    try:
        level = int(level)
        if level == 1:
            return random.randint(1, 10), random.randint(1, 10)
        elif level == 2:
            return random.randint(11, 99), random.randint(11, 99)
        elif level == 3:
            return random.randint(100, 999), random.randint(100, 999)
        else:
            print(type(level))
    except ValueError:
        # TODO: handle the ValueError
        ...


if __name__ == "__main__":
    main()
