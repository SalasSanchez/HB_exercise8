#!/usr/bin/env python

import sys
import random
import string

test_string = "Would you, could you in a house, Would you, could you with a mouse Would you, could you in a box Would you, could you with a fox Would you like green eggs and ham? Would you like them, Sam I Am?"


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    split_text = corpus.split()
    markov_dictionary = {}
    for i in range(len(split_text) - 2):
        # -2 because the last tuple has nothing following it.
        markov_tuple = split_text[i], split_text[i+1]
        #print markov_tuple
        if not markov_dictionary.get(markov_tuple):
            markov_dictionary[markov_tuple] = [split_text[i+2]]
            # +2 because the value is the word following the bigram [0, 1]
            #print "added entry for "+ str(markov_tuple)
        else:
            #print "Current dictionary value"+str(markov_dictionary[markov_tuple])
            markov_dictionary[markov_tuple].append(split_text[i+2])
            #print "New dictionary value"+str(markov_dictionary[markov_tuple])
    return markov_dictionary

test_d= make_chains(test_string)


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
   
    random_text = []

    first_t = random.choice(chains.keys())

    #Checks that the first word starts with upper case
    while str.istitle(first_t[0]) == False:
        first_t = random.choice(chains.keys())
        continue

    random_text.append(first_t[0])
    random_text.append(first_t[1])
    
    #TODO this creates a text of 12 words, should be generalized
    #TODO fix this so random text ends at natural break points
      
    for i in range(10):
        current_t = random_text[i], random_text[i+1]
        if chains.get(current_t) is None:
            break
        next_value = random.choice(chains.get(current_t))
        random_text.append(next_value)
       
    random_text = string.join(random_text)
    return random_text

make_text(test_d)


# def main():
#     args = sys.argv

#     # Change this to read input_text from a file
#     input_text = "Some text"

#     chain_dict = make_chains(input_text)
#     random_text = make_text(chain_dict)
#     print random_text

# if __name__ == "__main__":
#     main()

