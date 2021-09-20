def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #list for storing permutation for base case
    base_perm_list = []

    #list for storing permutation for recursive case
    recur_perm_list = []

    #if length of sequence is 2, append sequence permutations to base_perm_list:
    #return base_perm_list
    if len(sequence) == 2:
        base_perm_list.append(sequence)
        base_perm_list.append(sequence[::-1])
        return base_perm_list

    #else get permutations of sequence without first character:
    else:
        ans = get_permutations(sequence[1:len(sequence)])

        #for loop to get permutations of sequence with first character:
        for char in ans:

            #find first permutation with first char in front
            #append to recur_perm_list
            first_perm = sequence[0] + char
            recur_perm_list.append(first_perm)

            i = 0
            #while loop to get permutation with first char in between the other chars:
            while i < len(char):
                #if i is equal to length of char minus 1, break
                if i == len(char) - 1:
                    break

                #else if i is greater or equal to 1:
                elif i >= 1:
                    #find middle permutation by splitting sequentially from left to right
                    #increase i by 1
                    mid_perm = char[0:i+1] + sequence[0].join(char.split(char[0:i+1]))
                    i += 1
                    
                #else:  
                else:
                    #find middle permutation by splitting the second char, increase i by 1
                    mid_perm = char[i] + sequence[0].join(char.split(char[i]))
                    i += 1
                    
                #append middle permutation to recur perm list
                recur_perm_list.append(mid_perm)
            
            #find last perm with first char at the end of the word
            #append to recur_perm_list
            last_perm = char + sequence[0]
            recur_perm_list.append(last_perm)

        return recur_perm_list
    


if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

