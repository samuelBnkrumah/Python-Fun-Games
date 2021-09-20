import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    word_length = len(word)
    first_component = 0
    
    for char in word:
        first_component += SCRABBLE_LETTER_VALUES[char]

    second_component = (7*word_length - 3*(n-word_length))
    if second_component < 1:
        second_component = 1
        
    return first_component * second_component


    
    
# TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    #print()                             # print an empty line
        

    return ''

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    hand['*'] = 1

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word = word.lower()
    new_hand = hand.copy()
    for char in word:
        if char not in new_hand:
            new_hand[char] = 0
        else:
            new_hand[char] -= 1

    return new_hand

        
# TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    check = False
    new_hand = hand.copy()
    word = word.lower()
    if word in word_list:
        check = True
            
    for i in range (len(word)):
        word = list(word)
        if word[i] == '*':
            
            for char in VOWELS:
                word = list(word)
                word[i] = char
                word = ''.join(str(e) for e in word)
            
                if word in word_list:
                    check = True
                    break
                
        elif word[i] not in new_hand:
            check = False
            
        elif word[i] in new_hand and new_hand[word[i]] >= 1:
            new_hand[word[i]] -= 1
        elif new_hand[word[i]] == 0:
            check = False
        
    return check
    
    
# TO DO... Remove this line when you implement this function

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length = ''
    for char in hand:
        for i in range (hand[char]):
            length += char
    return (len(length))

    
    pass  # TO DO... Remove this line when you implement this function

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    total_score = 0
    hand_length = calculate_handlen(hand)
    
    # As long as there are still letters left in the hand:
    while hand_length > 0:
       
    
        # Display the hand
        print ('Current hand:', end = ' ')
        print (display_hand(hand))
        
        # Ask user for input
        user_input = input('Enter word, or "!!" to indicate that you are finished:')
        
        # If the input is two exclamation points:
        if user_input == '!!':
        
            # End the game (break out of the loop)
            print ('Total score for this hand:', total_score)
            print ('----------------------')
            break

            
        # Otherwise (the input is not two exclamation points):
        else:

            # If the word is valid:
            if is_valid_word(user_input, hand, word_list) == True:
    

                score = get_word_score(user_input, hand_length)
                total_score = score + total_score
                user_input = ""+ str(user_input) + ""

                # Tell the user how many points the word earned,
                print (user_input + ' '  + 'earned' + ' ' + str(score) +' ' + 'points.', 'Total:', str(total_score) + ' ' + 'points')
                print ()
                # and the updated total score

            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print ('That is not a valid word. Please choose another word.')
                print ()
                
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand (hand, user_input)
            hand_length = calculate_handlen(hand)
            
        if hand_length == 0:
            print ('You ran out of letters')
            print('Total score for this hand:', total_score)
            print ('----------------------')
         
    return total_score
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
   
    

    # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    Vowels_Consonants = 'aeioubcdfghjklmnpqrstvwxyz'
     
    # for every character in hand:
    for char in hand:
        
        # if char is same as letter:
        if char == letter:
            #randomly choose a new letter
            new_letter = random.choice(Vowels_Consonants)
            
            #if  new letter is same as letter:
            if new_letter == letter:
                #again randomly choose a new letter
                new_letter = random.choice(Vowels_Consonants)
                
            #for every character in hand
            for w in hand:
                #if new letter is same as character:
                if new_letter == w:
                    #again randomly generate a new letter
                    new_letter = random.choice(Vowels_Consonants)

            #add new letter to hand with the value of letter
            hand[new_letter] = hand[char]

            #break out of look
            break
        
    #delete letter from hand and return hand
    del(hand[char])
    return hand
    
# TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    #ask user for number of hands
    number_of_hands = int(input('Enter total number of hands: '))
    
    #keep track of total scores for hand series
    total_score_for_hand_series = 0

    #generate a hand and display it 
    hand = deal_hand(HAND_SIZE)
    print ('Current hand:', end = ' ')
    print (display_hand(hand))


    #set answer to hand substitution query to "no"
    hand_sub_default = "no"
    
    #set answer to replay hand query to "no"
    replay = 'no'                    

    #as long as number of hands is greater than zero
    while number_of_hands > 0:
     
        if number_of_hands == 0:
                break   
        
        #default hand_sub "no" asks user hand sub query :
        if hand_sub_default == 'no':
            #ask user if they want to substitute a letter in hand
            hand_sub_default = input('Would you like to substitute a letter? Please type Yes or No: ')
            hand_sub_default = hand_sub_default.lower()
            print()

            if hand_sub_default == 'yes':
                #ask which letter they would like to substitute
                letter_sub = input('Which letter would you like to replace: ')
                hand = substitute_hand(hand, letter_sub)
                hand_sub_default = 'yes'
                print()
                    
        #plays hand for every new hand or replay                      
        score_of_hand = play_hand(hand, word_list)

        #if replay is "yes":
        if replay == 'yes':
            total_score_for_hand_series += score_of_hand

        #decrease number of hands by 1
        number_of_hands -= 1

                         
        

        #default replay "no" asks user replay query :
        if replay == 'no':
           
            #ask user if they would like to replay hand
            replay = input('Would you like to replay the hand? ')
            replay = replay.lower()
            print()

            
                       
            #if replay is no:
            if replay == 'no':
                #deal new hand
                hand = deal_hand(HAND_SIZE)
                
                #print Current hand only when a letter has not been substituted
                if hand_sub_default == 'no':
                    print ('Current hand:', end = ' ')
                    print (display_hand(hand))
            
                total_score_for_hand_series += score_of_hand
                
            #else play previous hand again:
            elif replay == 'yes':
                #prints previous hand
                print ('Current hand:', end = ' ')
                print (display_hand(hand))

                #default hand_sub "no" asks user hand sub query :
                if hand_sub_default == 'no':
                    #ask user if they want to substitute a letter in hand
                    hand_sub_default = input('Would you like to substitute a letter? ')
                    hand_sub_default = hand_sub_default.lower()
                    print()

                    if hand_sub_default == 'yes':
                        #ask which letter they would like to substitute
                        letter_sub = input('Which letter would you like to replace: ')
                        hand = substitute_hand(hand, letter_sub)
                        hand_sub_default = 'yes'
                        print()
                    
                score_of_hand_replay = play_hand(hand, word_list)
                           
                #if score of replay is greater than previous play, add replay score to total score          
                if score_of_hand_replay > score_of_hand:
                    total_score_for_hand_series += score_of_hand_replay
                           
                
                #set replay to "yes" to prevent a second replay query
                replay = 'yes'
                hand = deal_hand(HAND_SIZE)

              #print Current hand only when number of hands is grater than zero
                if number_of_hands > 0 and hand_sub_default == 'no':
                    print ('Current hand:', end = ' ')
                    print (display_hand(hand))
                
                
        #else if number of hands is zero, break:
        elif number_of_hands == 0:
            break

    print("Total score over all hands: ", total_score_for_hand_series)
        
        
           
    
            

            
       
                    
# TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    #hand = {'a':1, 'c':1, 'f':1, 'i':1, '*':1, 't':1, 'x':1}
    #play_hand (hand, word_list)
