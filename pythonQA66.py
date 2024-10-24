# A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the
# following sentence one hundred times: “I will never spam my friends
# again.” Your program should number each of the sentences and it should
# make eight different random-looking typos.

import random 

def make_typo(sentence):
    typo_index = random.randint(0,len(sentence) -1)
    typo_char = random.choice('abcdefghijklmnopqrstuvwxyz')
    return sentence[:typo_index] +typo_char +sentence[typo_index+1:]
def write_sentence():
    sentence =" i am the great"
    typo_indices = random.sample(range(1,101),8)
    for i in range(1,101):
        if i in typo_indices:
            print(f"{i}. {make_typo(sentence)}")
        else:
            print(f"{i}. {sentence}")
write_sentence()