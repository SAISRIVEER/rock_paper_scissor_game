import random
random_number = random.randint(0,2)
print("Welcome to the game")
my_choice = input("Choose 'r' for 'Rock', 'p' for 'Paper','s' for 'Scissor': ")
choices = ['r', 'p', 's']
computer_choice = choices[random_number]
if my_choice in choices:
    print(f'Your choice is {my_choice} and computer\'s choice is {computer_choice}')
    if (computer_choice == my_choice):
        print("Match Draw")
    elif (computer_choice == 'r' and my_choice == 's'):
        print("You won!")
    elif (computer_choice == 'p' and my_choice == 'r'):
        print("You won!")
    elif (computer_choice == 's' and my_choice == 'p'):
        print("You won!")
    else:
        print("You lose")
else:
    print("You haven't choosed the correct input please replay the game and use correct input")