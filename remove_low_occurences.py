import re
from difflib import SequenceMatcher

cavernes = 'corpus_asimov_leaderboard/les_cavernes_d_acier/les_cavernes_d_acier.txt'
prelude = 'corpus_asimov_leaderboard/prelude_a_fondation/prelude_a_fondation.txt'

## FAIRE TOURNER ÇA SUR LES ALIAS!!!

FILE = cavernes
MIN_NB_OF_ITERATIONS = 3

def get_text(input_string):
    match = re.search(r'^\D+', input_string)
    if match:
        return match.group()
    else:
        return None
    
counter_char = {}

with open(FILE+'_CHARACTERS', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
for line in lines:
    text = get_text(line)
    if text not in counter_char:
        counter_char[text] = 1 
    else:
        counter_char[text] += 1

with open(BOOK+'_characters-clean.txt', 'a', encoding='utf-8') as file:
    for char in counter_char:
        if counter_char > 
            
    


