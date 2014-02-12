#!/usr/bin/env python

import sys
import random

test_string = "Would you, could you in a house, Would you, could you with a mouse Would you, could you in a box Would you, could you with a fox Would you like green eggs and ham? Would you like them, Sam I Am?"


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #save and split corpus on the whitespace 
    # create empty dictionary
    #open for loop:
    # if not dictionary.get(tuple):
            #dictionary[tuple] = [the word after]
    #else
        #d[tuple] = d[tuple].append[word that's after]
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



#print random.choice(test_d.keys())


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # create list that will become random text
    #pick starting point
    #(random_text[0], random_text[1]) = (key_part1, key_part2)

    #pick the random value of (key_part1, key_part2)
    #add this value to random_text[2]    
    # 
# randomly pick one key (tuples) from the dictionary
    random_text = []

    first_t = random.choice(chains.keys())
    random_text.append(first_t[0])
    random_text.append(first_t[1])
    
    #print random_text
    #TODO this creates a text of 12 words, should be generalized
    for i in range(10):
        current_t = random_text[i], random_text[i+1]
        next_value = random.choice(chains[current_t])
        random_text.append(next_value)
        print random_text

    #random_text.append(first_t)

    #print random_text


# pick the next word out of the value of the key, also randomly
    # identify the new tuple

    # next_value = [random.choice(chains[first_t])]
    # print next_value
    # random_text.append(next_value)
    # print random_text







    # Specify that we generate sentences of 5 tuples
    # TODO fix this so random text ends at natural break points
    # TODO fix things so random text starts at the start of a sentence
    
    


#    return "Here's some random text."

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

