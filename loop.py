run = True

def greeting_game():
    while run:
        name = input("Enter your name: ")
        print(f"Hello {name}! Good Morning!")

        user_input = input("Do you want to run the code again? (y/n)")

        if user_input == 'y':
            continue
        else:
            break


# For Loop
for i in range(1, 11):
    print(i, 'Hello Paris!')


# While Loop
i = 1
while i < 11:
    print(i, "Hello Paris!")
    i = i+1
