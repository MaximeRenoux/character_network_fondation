import re
from difflib import SequenceMatcher

cavernes = 'corpus_asimov_leaderboard/les_cavernes_d_acier/les_cavernes_d_acier.txt'
prelude = 'corpus_asimov_leaderboard/prelude_a_fondation/prelude_a_fondation.txt'

BOOK = cavernes

def get_text(input_string):
    match = re.search(r'^\D+', input_string)
    if match:
        return match.group()
    else:
        return None
    
counter_char = {}

with open(BOOK+'_CHARACTERS', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
for line in lines:
    text = get_text(line)
    if text not in counter_char:
        counter_char[text] = 1 
    else:
        counter_char[text] += 1
        
with open(BOOK+'_CHARACTER_LIST', 'w') as writeFile:
    for char in counter_char:
        writeFile.write(char+"\n")

