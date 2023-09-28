import pyfiglet
import random


def start_game():
    attempts = 7
    play_game = True
    words_list = [
            "computer",
            "programming",
            "hangman",
            "python",
            "developer",
            "keyboard",
            "software",
            "internet",
            "database",
            "algorithm",
            "variable",
            "function",
            "debugging",
            "version",
            "code",
            "project",
            "repository",
            "collaboration",
            "framework",
            "documentation"
        ]
    choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    selected_word = random.choice(words_list)
    not_guessed_word = ""
    for c in selected_word: 
        not_guessed_word += "_"
    guessed_word = not_guessed_word
    print(f"You have {attempts} attempts. Start guessing!")
    print(not_guessed_word)
    
    while(play_game): 
        user_choice = input("Please enter a letter: ").lower()
        if user_choice in choices: 
            choices.remove(user_choice)
            if user_choice not in selected_word:
                attempts -= 1
                print(f"You have {attempts} attempts left")
            for i in range(len(selected_word)): 
                if selected_word[i] == user_choice:
                    guessed_word = not_guessed_word[:i] + user_choice + not_guessed_word[i+1:]
                    not_guessed_word = guessed_word               
            print(guessed_word)
            if attempts == 0:
                print("You Lose.")
                play_game = False    
            if guessed_word == selected_word:
                play_again = input("You win! Play again? Y/N: ").lower()

                if play_again == "y":
                    start_game()
                else:
                    play_game = False
        else:
            print(f"You already selected {user_choice} . Select different letters")


# Function to display the menu with fancy text
def display_menu():
    banner = pyfiglet.figlet_format("Hangman Game")
    print(banner)
    print("Welcome to the Hangman Game!")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit")

# Function to handle user input for the menu
def get_menu_choice():
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Main menu loop
while True:
    display_menu()
    menu_user_choice = get_menu_choice()

    if menu_user_choice == "1":
        # Start the game
        print("Starting the game...")
        start_game()
    elif menu_user_choice == "2":
        # Display instructions
        print("Instructions:")
        print("Guess the word one letter at a time.")
        print("You have a limited number of incorrect guesses.")
        input("Press Enter to continue...")
    elif menu_user_choice == "3":
        # Quit the game
        print("Goodbye!")
        break

