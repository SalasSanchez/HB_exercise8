#!/usr/bin/env python

import sys
import random
import string
import os
import twitter

test_string = "Would you, could you in a house, Would you, could you with a mouse Would you, could you in a box Would you, could you with a fox Would you like green eggs and ham? Would you like them, Sam I Am?"

def create_tuple(text_list, start_index, length):
    n_tuple = (text_list[start_index],)
    for i in range(length-1):
        n_tuple = n_tuple + (text_list[start_index+i+1],)
    return n_tuple


def make_chains(corpus, n):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    split_text = corpus.split()
    for i in range(len(split_text)):
        split_text[i] = split_text[i].strip('"')

    markov_dictionary = {}
    for i in range(len(split_text) - n):
        # -2 because the last tuple has nothing following it.
        markov_tuple = create_tuple(split_text, i, n)
        #print markov_tuple
        if not markov_dictionary.get(markov_tuple):
            markov_dictionary[markov_tuple] = [split_text[i+n]]
            # +2 because the value is the word following the bigram [0, 1]
            #print "added entry for "+ str(markov_tuple)
        else:
            #print "Current dictionary value"+str(markov_dictionary[markov_tuple])
            markov_dictionary[markov_tuple].append(split_text[i+n])
            #print "New dictionary value"+str(markov_dictionary[markov_tuple])
    return markov_dictionary

#test_d= make_chains(test_string,3)
#print test_d

def start_sentence(chains):
    random_text = []
    first_t = random.choice(chains.keys())
    #Checks that the first word starts with upper case
    while str.istitle(first_t[0]) == False:
        first_t = random.choice(chains.keys())
        continue
    random_text.append(first_t[0])
    random_text.append(first_t[1])
    return random_text

def make_sentence(chains):
    #TODO Change so it will accept any n-gram
    random_text = start_sentence(chains)
    current_t = random_text[0], random_text[1]
    while True: 
        if chains.get(current_t) == None :
            break
        next_value = random.choice(chains.get(current_t))
        random_text.append(next_value)
            
        if next_value[-1] == "." or next_value[-1]== "!" or next_value[-1]== "?":
            break

        current_t = current_t[1], next_value

    return random_text

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    random_text = make_sentence(chains)

    while True:
        if len(string.join(random_text)) > 140:
            random_text = make_sentence(chains)
            continue
        if len(string.join(random_text)) >= 70:
            break
        else:
            roll = random.randint(1,3)
            if roll>=2:
                break
            else:
                random_text.extend(make_sentence(chains))
            
    

    random_text = string.join(random_text)
    return random_text

#make_text(test_d)


def main():
    script, filename1, filename2, ngram = sys.argv

    f = open(filename1)
    f2 = open(filename2)
    input_text1 = f.read()
    input_text2 = f2.read()
    f.close()
    f2.close()
    input_text = input_text1 + input_text2
    chain_dict = make_chains(input_text, int(ngram))
    random_text = make_text(chain_dict)
    print random_text


#if __name__ == "__main__":
 # main()

def sign_into_twitter():
    consumer_key = os.environ.get("TWITTER_API_KEY")
    consumer_secret = os.environ.get("TWITTER_API_SECRET")
    access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
    access_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
    api = twitter.Api(consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token,
        access_token_secret=access_secret)
    print api.VerifyCredentials()

sign_into_twitter()

def tweet_this(tweet):
    os.environ.get("TWITTER_API_KEY")
    pass



