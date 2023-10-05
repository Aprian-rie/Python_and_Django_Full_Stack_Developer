import random

random_number_1 = str(random.randint(0, 9))
random_number_2 = str(random.randint(0, 9))
random_number_3 = str(random.randint(0, 9))

random_number = [random_number_1,random_number_2,random_number_3]
number_string = ""
for rand_num in random_number:
    number_string += rand_num

def give_clue():
    if user_input[0] == random_number_1 or user_input[1] == random_number_2 or user_input[2] == random_number_3:
        print("Match")
    else:
        print(close())

def close():
    for num in user_input:
        if num in random_number:
            return "Close"
        else:
            return "Nope"

is_game_on = True
print("Welcome Code Breaker! Let's see if you can guess a 3 digit number!")
print("Code has been generated, please enter a 3 digit number")
print(random_number)
while is_game_on:
    user_input = (input("What is your guess: "))
    give_clue()

    if user_input == number_string:
        is_game_on = False

print("You Won")

