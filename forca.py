# Preencha a lista com os números mecanográficos dos autores.
AUTORES = [...]

letters_tuple = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , 'Ç')

def chooseRandomWord(options): # Choose a random word from an given list.
    import random
    return random.choice(options).upper()

def cleanInput(inp): # Clean spaces and put input in UPPER case.
    return inp.upper().replace(' ', '')
    

def play(word): # Play function, it starts the game.
    word_length = len(word) # Take the word length for the "_" system.
    while True:
        print('_' * word_length)
        while True: # Input treatment, minimizing future output problems. 
            letter_try = cleanInput(input('Try an letter > '))
            if len(letter_try) == 1 and letter_try in letters_tuple: # Verifying if it's really a unique and valid letter.
                break
            else:
                print('Give as an input an valid letter.') # "Error" message after treatment.
                
                
            
        
        
        
        
        
            
def main():
    from wordlist import words1, words2
    
    # Descomente a linha que interessar para testar
    words = words1              # palavras sem acentos nem cedilhas.
    #words = words2             # palavras com acentos ou cedilhas.
    #words = words1 + words2    # palavras de ambos os tipos
   
    # Escolhe palavra aleatoriamente
    secret = chooseRandomWord(words)
    play('Rhyan')


if __name__ == "__main__":
    main()

