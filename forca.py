# Preencha a lista com os números mecanográficos dos autores.
AUTORES = [...]

from time import sleep

letters_tuple = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , 'Ç')


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

def menu(dynamic_list_menu, wrong_letters_menu, try_number_menu):
        clear_terminal()
        print(''.join(dynamic_list_menu))
        print(f"Wrong: {'-'.join(wrong_letters_menu)}")
        print(f"Try number: {try_number_menu}")
    

def play(word): # Play function, it starts the game.
    # Defining the variables:
    word = clean_string(word)
    dynamic_list = ['_' for i in range(len(word))] # Setting up the dynamic list, it will change and help to print the result in every game part.
    try_number = 0
    wrong_letters = []
    # original_word = ...
    print('Word:', word)
    sleep(3)
    while True:
        menu(dynamic_list, wrong_letters, try_number)
        while True: # Input treatment, minimizing future output problems. 
            letter_try = clean_string(input('Try an letter > '))
            if len(letter_try) == 1 and letter_try in letters_tuple: # Verifying if it's really a unique and valid letter.
                break
            else:
                print('Give as input an valid letter.') # "Error" message after treatment.
                
        positions_list = search_letter_pos(letter_try, word) # The list of the positions that the letter is in the word
        
        try_number += 1
        
        if len(positions_list) != 0: # Verify if the player got an word letter.
            for p in positions_list: # True: Looping to update dynamic_list
                dynamic_list[p] = letter_try
        else:
            wrong_letters.append(letter_try) #False: append in wrong_letters list
            
        if dynamic_list.count('_') == 0: # Stopping the game if the player already did all letters.
            print(f'You won! The word is {word}!')
            break
                    
        
        
        
            
def main():
    from wordlist import words1, words2
    
    # Descomente a linha que interessar para testar
    words = words1              # palavras sem acentos nem cedilhas.
    #words = words2             # palavras com acentos ou cedilhas.
    #words = words1 + words2    # palavras de ambos os tipos
   
    # Escolhe palavra aleatoriamente
    secret = choose_random_word(words)
    play('Rhyan')


if __name__ == "__main__":
    main()

