import string
from Cipher_A import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words (WORDLIST_FILENAME)
        pass #delete this line and replace with your code here
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
        pass #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy_valid_words = self.valid_words.copy()
        return copy_valid_words
        pass #delete this line and replace with your code here

     
    
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        transpose_dict = {}
        i = 0

        #go through chars of VOWELS LOWER:
        for i in range (len(VOWELS_LOWER)):

            #if i is equal to length of VOWELS LOWER - 1, break
            if i == len(VOWELS_LOWER) - 1:
                break
            
            #if i == 1:
            if i == 1:
                #add i+1th VOWELS LOWER and VOWELS UPPER char to transpose dict. values are also i+1th char
                transpose_dict[VOWELS_LOWER[i+1]] = VOWELS_LOWER[i+1]
                transpose_dict[VOWELS_UPPER[i+1]] = VOWELS_UPPER[i+1]
              
            #else if i == 2:  
            elif i == 2:
                #add ith VOWELS LOWER and VOWELS UPPER char to transpose dict. values are also ith char
                transpose_dict[VOWELS_LOWER[i]] = VOWELS_LOWER[i]
                transpose_dict[VOWELS_UPPER[i]] = VOWELS_UPPER[i]
              
            #else:    
            else:
                #add ith VOWELS LOWER and VOWELS UPPER char to transpose dict. values are i+1th char
                transpose_dict[VOWELS_LOWER[i]] = VOWELS_LOWER[i+1]
                transpose_dict[VOWELS_UPPER[i]] = VOWELS_UPPER[i+1]
              
            
                #add i+1th VOWELS LOWER and VOWELS UPPER char to transpose dict. values are ith char
                transpose_dict[VOWELS_LOWER[i+1]] = VOWELS_LOWER[i]
                transpose_dict[VOWELS_UPPER[i+1]] = VOWELS_UPPER[i]
              
        
        #add lower and upper case consonants to transpose dict
        for i in range (len(CONSONANTS_LOWER)):
            transpose_dict[CONSONANTS_LOWER[i]] = CONSONANTS_LOWER[i]
            transpose_dict[CONSONANTS_UPPER[i]] = CONSONANTS_UPPER[i]
            
            
        return transpose_dict
        pass #delete this line and replace with your code here
    
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_message = ''
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        
        #for all char in self.message_text
        for char in self.message_text:
            
            #if char not in lowercase and uppercase letters, add char to encrypted message
            if char not in lowercase_letters and char not in uppercase_letters:
                encrypted_message += char

            #else, find value of char in transpose dict and add it to encrypted message    
            else:
                encrypted_message += transpose_dict[char]

        return encrypted_message
        
        pass #delete this line and replace with your code here
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)
        pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        permutations = get_permutations(VOWELS_LOWER)
    
        #go through permutations:
        for char in permutations:
            #build transpose dict with each vowel permutation
            transpose_dict = self.build_transpose_dict(char)
            
            #try to decrypt Encrypted message with transpose dict
            decrypted_message = self.apply_transpose(transpose_dict)
            
            #test whether decrypted message is a valid word, return decrypted message if True
            test = is_word(self.valid_words, decrypted_message)
            if test == True:
                return decrypted_message
                
        #return encrypted message if decrypted message is not a valid word
        return self.message_text
        
        pass #delete this line and replace with your code here
    

if __name__ == '__main__':

    # Example test case
    users_word = input ('Please enter your message: ')
    message = SubMessage(users_word)
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    #print("Original message:", message.get_message_text(), "Permutation:", permutation)
    #print("Expected encryption: froit")
    print("Encrypted Message:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
   
