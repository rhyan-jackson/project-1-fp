# Preencha a lista com os números mecanográficos dos autores.
AUTORES = [120495, 115372]

# MÓDULOS EXTRA: unidecode
# pip install unidecode

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
        title_static()
        man.print()
        print(''.join(dynamic_list_menu))
        print(f"Wrong: {'-'.join(wrong_letters_menu)}")
        print(f"Try number: {try_number_menu}")
    
def welcome(static=False): # This is the function that does the animation in the terminal (visual feature, not much to explain about)
    if not static:
        import sys
        from hangman_string import hangman_string

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
        
def title_static(): # This function returns an static version of welcome_animation()
    from hangman_string import hangman_string_static
    print(hangman_string_static)

def try_again(): # Function used to do the "try again"'s after every game finish.
    option = None
    while not option in range(1, 6):
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
        
        try: option = int(input('Input > '))
        except ValueError: print('Invalid option. Please pick one above.'); sleep(2); clear_terminal(); title_static()
        else:
            if option in range(1, 6):
                if option == 5: option = 0 # Used to standardize the def's output, makes treatment logic easier.
                return option
            else:
                print('Invalid option. Please pick one above.'); sleep(2); clear_terminal(); title_static()
            
        
def word_choose_by_difficulty(difficulty=0):
    from wordlist import words1, words2
    words_easy = words1               # palavras sem acentos nem cedilhas.
    words_medium = words2             # palavras com acentos ou cedilhas.
    words_hard = words1 + words2      # palavras de ambos os tipos
    
    while not difficulty in range(1, 5):
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
        try: difficulty = int(input('Input > '))
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
    
        # elif option1 == 1:
        #     secret = choose_random_word(words_easy)
        #     play(secret)
        #     option2 = try_again()
        #     if option2 == 1:
        #         play(secret)
        #     elif option2 == 2:
        #         title_static()
        #     elif option2 == 3:
        #         break
            
        # elif option1 == 2:
        #     secret = choose_random_word(words_medium)
        #     play(secret)
        #     option2 = try_again()
        #     if option2 == 1:
        #         play(secret)
        #     elif option2 == 2:
        #         title_static()
                
        #     elif option2 == 3:
        #         break
            
        # elif option1 == 3:
        #     secret = choose_random_word(words_hard)
        #     play(secret)
        #     option2 = try_again()
        #     if option2 == 1:
        #         play(secret)
        #     elif option2 == 2:
        #         title_static()
        #     elif option2 == 3:
        #         break
        # elif option1 == 4:
        #     print('Thanks for playing our game!')
        #     break
        # elif option1 >= 5:
        #     print('Invalid option. Please pick an option above.')
    

    
def play(word): # Play function, it starts the game.
    # Defining the variables:
    word = clean_string(word)
    man = Man(cartoon_list=cartoon_list) # Defining the Hangman.
    dynamic_list = ['_' for i in range(len(word))] # Setting up the dynamic list, it will change and help to print the result in every game part.
    try_number = 0
    wrong_letters = []
    # original_word = ...
    #print('Word:', word)
    
    while True: # Calling the menu.
        while True: # Input treatment, minimizing future output problems.
            menu(dynamic_list, wrong_letters, try_number, man) 
            letter_try = clean_string(input('Try an letter > '))
            if len(letter_try) == 1 and letter_try in letters_tuple: # Verifying if it's really a unique and valid letter.
                break
            else:
                print('Give as input an valid letter.') # "Error" message after treatment.
                sleep(1.2)
                clear_terminal()
                
        positions_list = search_letter_pos(letter_try, word) # The list of the positions that the letter is in the word
        
        if letter_try in dynamic_list or letter_try in wrong_letters:
            print(color(31, 'You\'ve already tried this.'))
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
            clear_terminal()
            title_static()
            print(f'You won!')
            break
        elif len(wrong_letters) > 5:
            clear_terminal()
            title_static()
            print(f'You lose!')
            break 
                 
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
def main():
    static = False
    while True:
    # Welcome Animation
        clear_terminal()
        welcome(static)
        static = True
    # Pergunta dificuldade
        word, difficulty = word_choose_by_difficulty()
        if (word, difficulty) == (0, 0):
            break
    # Play com dificuldade
        word = 'rhyan'
        play(word)
        # print('play', word)
    # Menu: Repetir, Nova palavra mesma dificuldade, Mesma palavra, Sair.
        while True:
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