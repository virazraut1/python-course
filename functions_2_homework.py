

def find_greater (a, b, c):
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > c:
        print(f"{b} is greater then {c}")
    else:
        print(f"{c} is greater than {a}")


find_greater(10, 50, 30)


def find_greater_again(a, b, c):
    if (a > b) and (a > c):
        print(f'{a} is the Greatest.')
    elif (b > a) and (b > c):
        print(f'{b} is the Greatest')
    else:
        print(f'{c} is the greatest')

    # Another method

    if a > b:
        if a > c:
            print("A is the greatest")
        else:
            print("C is the greatest")
    else:
        print("B is the greatest")

find_greater_again(10, 50, 30)
