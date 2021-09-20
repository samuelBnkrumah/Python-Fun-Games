import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    test = 'True'

    for char in secret_word:
            if char not in letters_guessed:
                test = 'False'           
    return test
        

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ''

    for char in secret_word:
        if char in letters_guessed:
            guessed_word += char
        else:
            guessed_word += '_ '
            
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabets = string.ascii_lowercase
    remaining_letters = ''
    for char in alphabets:
        if char in letters_guessed:
            remaining_letters += ''
        else:
            remaining_letters += char
    return remaining_letters


def hangman(secret_word):
    length_of_word = str(len(secret_word))
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print ('Welcome to the Hangman Game. Let us play!')
    print ('I am thinking of a word that is' + ' '+ length_of_word + ' '+ 'letters long')
    print ('You have 3 warnings left')   
    print ('-------------------')
    
    secret_word_list = []
    for char in secret_word:
        if char not in secret_word_list:
            secret_word_list += char
    
    letters_guessed = []
    number_of_guesses = 6
    warnings = 3
    while number_of_guesses > 0:
        
    
        available_letters = get_available_letters (letters_guessed)
        print ('You have' +' ' + str(number_of_guesses) + ' ' + 'guesses left')
        print ('Available letters:', available_letters)
        
        guess = input ('Please guess a letter: ')
        guess = guess.lower()
        letters_guessed += guess
       
        
        alphabets = string.ascii_lowercase
        vowels = ['a','e', 'i', 'o', 'u']
        guessed_word = get_guessed_word (secret_word, letters_guessed)
        
        if guess not in alphabets:
            warnings -= 1
            if warnings < 0:
                number_of_guesses -= 1
                print ('Oops! That is not a valid letter. You have no warnings left so you lose one guess:', guessed_word)
                print ('-----------------')
            else:
                print ('Oops! That is not a valid letter. You have' + ' ' + str(warnings) + ' ' + 'warnings left: ', guessed_word)
                print ('-----------------')
                
        elif guess in secret_word_list:
            print ('Good guess: ', guessed_word)
            print ('-----------------')
        elif guess not in secret_word_list:
            print ('Oops! That letter is not in my word:', guessed_word)
            print ('-----------------')
            number_of_guesses -= 1
        elif guess in alphabets and vowels and not secret_word_list:
            print ('Oops! That letter is not in my word:', guessed_word)
            print ('-----------------')
            number_of_guesses -= 2
        
        elif guess in alphabets and letters_guessed:
            warnings -= 1
            if warnings < 0:
                number_of_guesses -= 1
                print ('Oops! You have already guessed that letter. You have no warnings left so you lose one guess:', guessed_word)
                print ('-----------------')
            else:
                print ('Oops! You have already guessed that letter. You now have' + ' ' + str(warnings) +':', guessed_word)
                print ('-----------------')
        

        check = is_word_guessed(secret_word, letters_guessed)
        if check == 'True':
            print ('Congratulations, you won!')
            print ('Your total score for this game is: ', number_of_guesses * len (secret_word_list))
            break
        elif number_of_guesses == 0:
            print ('Sorry, you ran out of guesses. The word was' + ' ' + secret_word)
            
                   

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    my_word = ''.join(my_word.split())
    other_word_list = []
    my_word_list =[]
    check = 'True'
    
    for char in other_word:
        other_word_list += char
        
    for char in my_word:
        my_word_list += char
        
    if len(my_word) != len(other_word):
        check = 'False'
    else:
        for i in range(len(my_word)):
            if my_word_list[i] != '_' and my_word_list[i] != other_word_list[i]:
                check = 'False'
    return check
            
        



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = ()
    for word in wordlist:
        if match_with_gaps (my_word, word) == 'True':
            possible_matches += (word,)
    if len(possible_matches) == 0:
        return 'No matches found'
    else:
        for char in possible_matches:
            print (char, end = ' ')
    return ''
            


def hangman_with_hints(secret_word):
    length_of_word = str(len(secret_word))
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print ('Welcome to the Hangman Game. Let us play!')
    print ('I am thinking of a word that is' + ' '+ length_of_word + ' '+ 'letters long')
    print ('You have 3 warnings left')   
    print ('-------------------')
    
    secret_word_list = []
    for char in secret_word:
        if char not in secret_word_list:
            secret_word_list += char
    
    letters_guessed = []
    number_of_guesses = 6
    warnings = 3
    while number_of_guesses > 0:
        
    
        available_letters = get_available_letters (letters_guessed)
        print ('You have' +' ' + str(number_of_guesses) + ' ' + 'guesses left')
        print ('Available letters:', available_letters)
        
        guess = input ('Please guess a letter: ')
        guess = guess.lower()
        letters_guessed += guess
       
        
        alphabets = string.ascii_lowercase
        vowels = ['a','e', 'i', 'o', 'u']
        guessed_word = get_guessed_word (secret_word, letters_guessed)

        if guess == '*':
            print ('Possible matches are:')
            print (show_possible_matches(guessed_word))
            print ('---------------')
            
        
        elif guess not in alphabets:
            warnings -= 1
            if warnings < 0:
                number_of_guesses -= 1
                print ('Oops! That is not a valid letter. You have no warnings left so you lose one guess:', guessed_word)
                print ('-----------------')
            else:
                print ('Oops! That is not a valid letter. You have' + ' ' + str(warnings) + ' ' + 'warnings left: ', guessed_word)
                print ('-----------------')
                
        elif guess in secret_word_list:
            print ('Good guess: ', guessed_word)
            print ('-----------------')
        elif guess not in secret_word_list:
            print ('Oops! That letter is not in my word:', guessed_word)
            print ('-----------------')
            number_of_guesses -= 1
        elif guess in alphabets and vowels and not secret_word_list:
            print ('Oops! That letter is not in my word:', guessed_word)
            print ('-----------------')
            number_of_guesses -= 2
        
        elif guess in alphabets and letters_guessed:
            warnings -= 1
            if warnings < 0:
                number_of_guesses -= 1
                print ('Oops! You have already guessed that letter. You have no warnings left so you lose one guess:', guessed_word)
                print ('-----------------')
            else:
                print ('Oops! You have already guessed that letter. You now have' + ' ' + str(warnings) +':', guessed_word)
                print ('-----------------')
       
        
        check = is_word_guessed(secret_word, letters_guessed)
        if check == 'True':
            print ('Congratulations, you won!')
            print ('Your total score for this game is: ', number_of_guesses * len (secret_word_list))
            break
        elif number_of_guesses == 0:
            print ('Sorry, you ran out of guesses. The word was' + ' ' + secret_word)
            




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
