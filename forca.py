# Preencha a lista com os números mecanográficos dos autores.
AUTORES = [120495, 115372]

# MÓDULOS EXTRA: unidecode
# pip install unidecode

from time import sleep # Imports sleep module used to suspend the execution for the given seconds.
import sys # This helps cleaning and updating the terminal.
from unidecode import unidecode # Unidecode is used for transforming words with accent in base words.
from hangman_string import * # Imports some strings.
from wordlist import words1, words2 # Imports the wordlists given.

letters_tuple = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , 'Ç', 'À', 'È', 'Ì', 'Ò', 'Ù', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ý', 'Â', 'Ê', 'Î', 'Ô', 'Û', 'Ã', 'Õ')

cartoon_list = [
    """
    _____
    |   |
    |   
    |  
    |
    |_______ 
    """,
    """
    _____
    |   |
    |   O
    | 
    |
    |_______
    """,
    """
    _____
    |   |
    |   O
    |   |
    |
    |_______
    """,
    """
    _____
    |   |
    |   O
    |  /|
    |
    |_______
    """,
    """
    _____
    |   |
    |   O
    |  /|\\
    |
    |_______
    """,
    """
    _____
    |   |
    |   O
    |  /|\\
    |  /
    |_______
    """,
    """
    _____
    |   |
    |   O
    |  /|\\
    |  / \\
    |_______
    """
]

class Man: # Hangman Man object, it will change and print the man during the game.
    def __init__(self, cartoon_list):
        self.phase = 0
        self.cartoon_list = cartoon_list
    
    def print(self):
        print(self.cartoon_list[self.phase])
    
    
    def increase_phase(self):
        self.phase += 1

def color(id, msg): # Changes the color of a message and returns it.
    return f'\033[{id}m{msg}\033[m'

def clear_terminal(): # Clear the terminal
    import os
    os.system('clear')

def choose_random_word(options): # Choose a random word from a given list.
    import random
    return random.choice(options).upper()

def clean_string(inp): # Clean spaces and put input in UPPER case.
    return inp.upper().replace(' ', '')

def search_letter_pos(letter_try, word):
    positions = [] # Creates the list of the positions that the letter is present in word
    for pos, letter in enumerate(word): # Searching for the position of the letters
        if letter == letter_try:
            positions.append(pos)
    return positions # Return a list with the positions of the letters in a word, if empty, the letter_try not in word

def menu(dynamic_list_menu, wrong_letters_menu, try_number_menu, man): # The Menu. This is how the game will be displayed in the script.
        clear_terminal()
        title_static()
        man.print()
        print(''.join(dynamic_list_menu))
        print(f"Wrong: {'-'.join(wrong_letters_menu)}")
        print(f"Try number: {try_number_menu}")
    
def welcome(static=False): # This is the function that does the animation in the terminal (visual feature, not much to explain about). It uses the string with characters from the Extended ASCII Table from the file 'hangman_string.py' and prints it to the terminal.
    if not static:
        codes = (7, 3)
        pos = 0
        for x,i in enumerate(hangman_string):
            if x % 7 == 0:
                if pos > len(codes) - 1:
                    pos = 0
                print(f'\033[3{codes[pos]}m', end='')
                pos += 1
            sys.stdout.flush()
            print(i, end='')
            sleep(0.002)
        sleep(0.8)
        print('\033[m')
    else:
        title_static()
        
def title_static(): # This function returns a static version of welcome_animation()
    print(hangman_string_static)

def try_again(): # Function used to do the "try again"'s after every game finish.
    option = None
    while not option in range(1, 6): # Menu of try again
        option = None
        print(
            '''
            Please, choose an option below.
            
            (1) > Try again the last word
            (2) > Try another word in the same difficulty
            (3) > Change difficulty
            (4) > Result of the last game
            (5) > Exit
            '''
        )
        
        try: option = int(input('Input > ')) # This type of treatment is common in the input's parts, it helps to treat the user input with accuracy.
        except ValueError: print('Invalid option. Please pick one above.'); sleep(2); clear_terminal(); title_static()
        else:
            if option in range(1, 6):
                if option == 5: option = 0 # Used to standardize the def's output, makes treatment logic easier.
                return option
            else:
                print('Invalid option. Please pick one above.'); sleep(2); clear_terminal(); title_static()
            
        
def word_choose_by_difficulty(difficulty=0): # Function to choose the "difficulty" of the game. It imports the strings from the file 'wordlist.py'.
    words_easy = words1               # No accented words.
    words_medium = words2             # Accented words.
    words_hard = words1 + words2      # Both.
    
    while not difficulty in range(1, 5): # Difficulty selection menu.
        difficulty = None
        clear_terminal()
        title_static()
        print(
            '''
            Insert in the difficulty that you want to play.
            
            (1) > Easy
            (2) > Medium
            (3) > Hard
            (4) > Quit game
            
            '''
        )
        try: difficulty = int(input('Input > ')) # The same treatment of try_again() function.
        except ValueError: print('Invalid option. Please pick one above.'); sleep(2); clear_terminal(); title_static()
        else:
            if difficulty in range(1, 5):
                break
            else: print('Invalid option. Please pick one above.'); sleep(2); clear_terminal(); title_static()
    if difficulty == 1:
        word = choose_random_word(words_easy)
    elif difficulty == 2:
        word = choose_random_word(words_medium)
    elif difficulty == 3:
        word = choose_random_word(words_hard)
    elif difficulty == 4:
        return (0, 0)
    return word, difficulty
    
def play(word): # Play function, it starts the game.
    # Defining the variables:
    word = clean_string(word)
    no_accent_word = unidecode(word)
    man = Man(cartoon_list=cartoon_list) # Defining the Hangman. (This is POO, search for it in google if necessary.)
    dynamic_list = ['_' for i in range(len(word))] # Setting up the dynamic list, it will change and help to print the result in every game part.
    try_number = 0
    wrong_letters = []
    original_word = [x for x in word]
    #print('Word:', word)
    
    while True: # Calling the menu.
        while True: # Input treatment, minimizing future output problems.
            menu(dynamic_list, wrong_letters, try_number, man) # Calls menu function, giving the parameters.
            letter_try = unidecode(clean_string(input('Try an letter > '))) # This is the letter that the player inputs.
            if len(letter_try) == 1 and letter_try in letters_tuple: # Verifying if it's really a unique and valid letter.
                break
            else:
                print(color(31, 'Give as input an valid letter.')) # "Error" message after treatment.
                sleep(1.2)
                clear_terminal()
                
        positions_list = search_letter_pos(letter_try, no_accent_word) # The list of the positions that the letter is in the word
        
        if letter_try in dynamic_list or letter_try in wrong_letters: # Verifying if the letter was already tried in game session.
            print(color(31, 'You\'ve already tried this.'))
            sleep(2)
        else:
            if len(positions_list) != 0: # Verify if the player got an word letter.
                    for p in positions_list: # True: Looping to update dynamic_list
                        dynamic_list[p] = original_word[p]
            else:
                wrong_letters.append(letter_try) #False: append in wrong_letters list
                man.increase_phase() # Increase the man's phase.
            try_number += 1
        if dynamic_list.count('_') == 0: # Stopping the game if the player already did all letters.
            clear_terminal()
            title_static()
            print(color(32, f'You won!'))
            break
        elif len(wrong_letters) > 5:
            clear_terminal()
            title_static()
            print(color(31, f'You lose!'))
            if len(sys.argv) > 1:
                while True:
                    print(
            '''
            Do you want to reveal the last played word?
                        
            (1) > Yes
            (2) > No
                            
            '''
                    )
                    try: answer = int(input('Input > '))
                    except ValueError: print('Invalid option. Please pick one above.'); sleep(2); clear_terminal(); title_static()
                    else:
                        if answer in (1, 2):
                            break
                        else: print('Invalid option. Please pick one above.'); sleep(2); clear_terminal(); title_static()
                if answer == 1:
                    print(f'The word was: {word}')
            break 
                 
                 
def main(): # The main function. It's the "cerebrus" of the game.
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        word = choose_random_word(words)
        welcome()
        play(word)
    else:
        static = False
        while True:
        # Welcome Animation
            clear_terminal()
            welcome(static)
            static = True
        # Menu to choose difficulties
            word, difficulty = word_choose_by_difficulty()
            if (word, difficulty) == (0, 0):
                break
        # Game itself        
            play(word)
        # After Game Menu: Repeat, New word with same difficulty, Change difficulty, Reveal the word, Exit.
            while True: # Looping and executing what the player calls in the try_again() function menu.
                option_try_again = try_again()
                if option_try_again == 1:
                    play(word)
                elif option_try_again == 2:
                    word, difficulty = word_choose_by_difficulty(difficulty)
                    play(word)
                elif option_try_again == 3:
                    break
                elif option_try_again == 4:
                    print(word)
                elif option_try_again == 0:
                    break
            if option_try_again == 0: break

main()
clear_terminal(); title_static()
print(color(33, "Thank you for playing!"))
sleep(2)