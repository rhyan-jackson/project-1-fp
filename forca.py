# Preencha a lista com os números mecanográficos dos autores.
AUTORES = [...]

from time import sleep

letters_tuple = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , 'Ç')

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

def color(id, msg): # Return an coloured message
    return f'\033[{id}m{msg}\033[m'

def clear_terminal(): # Clear the terminal
    import os
    os.system('clear')

def choose_random_word(options): # Choose a random word from an given list.
    import random
    return random.choice(options).upper()

def clean_string(inp): # Clean spaces and put input in UPPER case.
    return inp.upper().replace(' ', '')
    # IMPLEMENTAR TRANSFORMAR ACENTOS EM LETRAS NORMAIS

def search_letter_pos(letter_try, word):
    positions = [] # Creates the list of the positions that the letter is present in word
    for pos, letter in enumerate(word): # Searching for the position of the letters
        if letter == letter_try:
            positions.append(pos)
    return positions # Return a list with the positions of the letters in a word, if empty, the letter_try not in word

def menu(dynamic_list_menu, wrong_letters_menu, try_number_menu, man): # This is how the game will be displayed in the script.
        clear_terminal()
        man.print()
        print(''.join(dynamic_list_menu))
        print(f"Wrong: {'-'.join(wrong_letters_menu)}")
        print(f"Try number: {try_number_menu}")
    
def welcome_animation():
    import sys
    from hangman_string import hangman_string

    codes = (0, 3)
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
    sleep(5)
    print('\033[m')
def play(word): # Play function, it starts the game.
    # Defining the variables:
    word = clean_string(word) #
    man = Man(cartoon_list=cartoon_list) # Defining the Hangman.
    dynamic_list = ['_' for i in range(len(word))] # Setting up the dynamic list, it will change and help to print the result in every game part.
    try_number = 0
    wrong_letters = []
    # original_word = ...
    #print('Word:', word)
    sleep(3)
    
    welcome_animation()
    
    while True:
        menu(dynamic_list, wrong_letters, try_number, man) # Calling the menu.
        while True: # Input treatment, minimizing future output problems. 
            letter_try = clean_string(input('Try an letter > '))
            if len(letter_try) == 1 and letter_try in letters_tuple: # Verifying if it's really a unique and valid letter.
                break
            else:
                print('Give as input an valid letter.') # "Error" message after treatment.
                
        positions_list = search_letter_pos(letter_try, word) # The list of the positions that the letter is in the word
        
        if letter_try in dynamic_list or letter_try in wrong_letters:
            print(color(31, 'Youve already tried this.'))
            sleep(2)
        else:
            if len(positions_list) != 0: # Verify if the player got an word letter.
                    for p in positions_list: # True: Looping to update dynamic_list
                        dynamic_list[p] = letter_try
            else:
                wrong_letters.append(letter_try) #False: append in wrong_letters list
                man.increase_phase() # Increase the man's phase.
            try_number += 1
        if dynamic_list.count('_') == 0: # Stopping the game if the player already did all letters.
            print(f'You won! The word is {word}!')
            break
        elif len(wrong_letters) > 5:
            print(f'YOU LOSE! Thw word was {word}.')
            break
       
       
def keep_playing():
    print('Do you want to keep playing?')
    print('1 - Continue')
    print('2 - Change difficulty')
    print('3 - Exit')
    x = 0
    while (x < 1 or x > 3):
        x = int(input(''))
    if x < 1:
        print('Invalid option. Please pick an option above.') 
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        print('Thanks for playing our game!')
        return 3
    elif x > 3:
        print('Invalid option. Please pick an option above.')
    
    
                 
'''
def wordlist_words():
    from wordlist import words1, words2

    # Descomente a linha que interessar para testar
    words_easy = words1              # palavras sem acentos nem cedilhas.
    words_medium = words2            # palavras com acentos ou cedilhas.
    words_hard = words1 + words2     # palavras de ambos os tipos
''' 

'''        
def main():
    # Descomente a linha que interessar para testar
    words_easy = words1               # palavras sem acentos nem cedilhas.
    words_medium = words2             # palavras com acentos ou cedilhas.
    words_hard = words1 + words2      # palavras de ambos os tipos
   
    # Escolhe palavra aleatoriamente
    secret = choose_random_word(words_easy)
    play(secret)

main()
'''
'''
wordlist_words()
'''
from wordlist import words1, words2
words_easy = words1               # palavras sem acentos nem cedilhas.
words_medium = words2             # palavras com acentos ou cedilhas.
words_hard = words1 + words2      # palavras de ambos os tipos

option = 0
welcome_animation()
while (option != 4) :
    print('|----------------------------------------------------------------------------------------------------------------------------------------------------|')
    print('|                                                 Welcome to HangMan Game! Choose your difficulty:                                                   |')
    print('|                                                                     1 - Easy                                                                       |')
    print('|                                                                     2 - Medium                                                                     |')
    print('|                                                                     3 - Hard                                                                       |')
    print('|                                                                     4 - Quit Game                                                                  |')
    print('|----------------------------------------------------------------------------------------------------------------------------------------------------|')
    option1 = int(input(''))
    option2 = 0
    
    if option1 <= 0:
        print('Invalid option. Please pick an option above.')
        continue
    elif option1 == 1:
        secret = choose_random_word(words_easy)
        play(secret)
        option2 = keep_playing()
        if option2 == 1:
            play(secret)
        elif option2 == 2:
            welcome_animation()
            continue
        elif option2 == 3:
            break
        
    elif option1 == 2:
        secret = choose_random_word(words_medium)
        play(secret)
        option2 = keep_playing()
        if option2 == 1:
            play(secret)
        elif option2 == 2:
            welcome_animation()
            continue
        elif option2 == 3:
            break
        
    elif option1 == 3:
        secret = choose_random_word(words_hard)
        play(secret)
        option2 = keep_playing()
        if option2 == 1:
            play(secret)
        elif option2 == 2:
            welcome_animation()
            continue
        elif option2 == 3:
            break
    elif option1 == 4:
        print('Thanks for playing our game!')
        break
    elif option1 >= 5:
        print('Invalid option. Please pick an option above.')
        continue
    
