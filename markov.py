"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    read_file = open(file_path).read()

    return read_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()

    chains = {}

    for i in range(len(words) - 1):
     
        new_tuple = tuple([words[i], words[i+1]])
     
        if new_tuple in chains:
            if new_tuple == tuple([words[-2], words[-1]]):
                chains[new_tuple] = None
                break
            chains[new_tuple].append(words[i+2])
        else:
            if new_tuple == tuple([words[-2], words[-1]]):
                chains[new_tuple] = None
                break
            chains[new_tuple] = [words[i+2]]

    # print(chains)

    return chains


def make_text(chains):
    """Return text from chains."""
    import random

    words = []

    random_tuple = random.choice(list(chains.keys()))

    while chains[random_tuple] != None:
        words.append(random_tuple[0])
        chosen_value = random.choice(chains[random_tuple])
        random_tuple = (random_tuple[1], chosen_value)
    
    words.extend(random_tuple)

#we want to pick a random key from the dict that is a tuple, so we know where to start
#from tuple, add index[0] to a list, then use index[1] and value to make a "new tuple"
#value should be "random"
#use that new tuple to find the next tuple randomly and do the same thing, adding index [0] to list
#using index[1] to find the next tuple

#will end when hits "None," so length of randomly generated list  will vary
#hint: while loop? ask for clarification if needed

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
