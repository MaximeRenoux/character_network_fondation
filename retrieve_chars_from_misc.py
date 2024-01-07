import re
from difflib import SequenceMatcher

cavernes = 'corpus_leaderboard/les_cavernes_d_acier/les_cavernes_d_acier.txt'
prelude = 'corpus_leaderboard/prelude_a_fondation/prelude_a_fondation.txt'
fondation_et_empire = 'Corpus_ASIMOV/Fondation_et_empire_sample-cleaned'

BOOK = cavernes

COMMON_WORD_MINIMUM_LENGTH = 3
min_iteration = 3

def get_text(input_string):
    match = re.search(r'^\D+', input_string)
    if match:
        return match.group()
    else:
        return None
    
def have_common_word(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())
    
    common_words = words1.intersection(words2)
    
    long_enough = False
    for word in common_words:
        if len(word) >= COMMON_WORD_MINIMUM_LENGTH:
            long_enough = True
    if long_enough:
        return len(common_words) > 0
    else:
        return False
    
counter_char = {}
counter_misc = {}

"""Counting occurences of each CHAR entity"""

with open(BOOK+'_CHARACTERS', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
for line in lines:
    text = get_text(line)
    if text not in counter_char:
        counter_char[text] = 1 
    else:
        counter_char[text] += 1
        
# for item in counter_char:
#     if counter_char[item] >= min_iteration:
#         print(item+' : '+str(counter_char[item]))    
# print('\n\n\n\n\n')
        
        
"""Counting occurences of each MISC entity"""

with open(BOOK+'_MISC', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
for line in lines:
    text = get_text(line)
    if text not in counter_misc:
        counter_misc[text] = 1 
    else:
        counter_misc[text] += 1
        
# for item in counter_misc:
#     if counter_misc[item] >= min_iteration:
#         print(item+' : '+str(counter_misc[item]))

"""Adding MISC entities to CHARACTER file"""

with open(BOOK+'_MISC', 'r', encoding='utf-8') as originalMiscFile:
    linesMisc = originalMiscFile.readlines()
with open(BOOK+'_CHARACTERS', 'r', encoding='utf-8') as originalCharFile:
    linesChar = originalCharFile.readlines()
    

with open(BOOK+'_CHARACTERS', 'a', encoding='utf-8') as file:
    file.write('-------------\n')
    for misc in counter_misc:
        for char in counter_char:
            if counter_misc[misc] >= min_iteration  and counter_char[char] < min_iteration and have_common_word(misc, char):
                print("----")
                print('Misc : '+misc+' : '+str(counter_misc[misc]))
                print('Perso : '+char+' : '+str(counter_char[char]))
                print("----")
                
                letter_count = 0
                for c in char:
                    if c.isalpha():
                        letter_count += 1
                
                if letter_count >= COMMON_WORD_MINIMUM_LENGTH:
                        
                    for line in linesMisc:
                        if get_text(line) == misc:
                            file.write(line)
                            
                    for line in linesChar:
                        if get_text(line) == char:
                            file.write(line)
            
                