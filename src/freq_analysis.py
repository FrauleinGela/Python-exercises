import string
# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.

def freq_analysis(message):
    found_letters = {}
    freq_list = []
    abc = string.ascii_lowercase
    i =0
    while True:
        if i >= len(abc):
            break
        found_letters[abc[i]] = 0
        i+=1
        
    for letter in message:
        if not (letter).islower():
            return False
        if letter in found_letters:
            found_letters[letter] += 1
        else:
            return False  
    for attr, value in sorted(found_letters.items()):
        freq_list.append(value/float(len(message)))
    return freq_list



#Tests

print(freq_analysis("abcd"))
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print(freq_analysis("adca"))
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print(freq_analysis('bewarethebunnies'))
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
