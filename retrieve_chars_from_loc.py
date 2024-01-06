import re
from difflib import SequenceMatcher

cavernes = 'corpus_leaderboard/les_cavernes_d_acier/les_cavernes_d_acier.txt'
prelude = 'corpus_leaderboard/prelude_a_fondation/prelude_a_fondation.txt'
fondation_et_empire = 'Corpus_ASIMOV/Fondation_et_empire_sample-cleaned'

BOOK = prelude

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
        if len(word) >= 3:
            long_enough = True
    if long_enough:
        return len(common_words) > 0
    else:
        return False
    
counter_char = {}
counter_loc = {}
min_iteration = 3

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
        
with open(BOOK+'_LOCATIONS', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
for line in lines:
    text = get_text(line)
    if text not in counter_loc:
        counter_loc[text] = 1 
    else:
        counter_loc[text] += 1
        
# for item in counter_loc:
#     if counter_loc[item] >= min_iteration:
#         print(item+' : '+str(counter_loc[item]))

with open(BOOK+'_LOCATIONS', 'r', encoding='utf-8') as originalLocationsFile:
    linesLocations = originalLocationsFile.readlines()
with open(BOOK+'_CHARACTERS', 'r', encoding='utf-8') as originalCharFile:
    linesChar = originalCharFile.readlines()
    


with open(BOOK+'_CHARACTERS', 'a', encoding='utf-8') as file:
    file.write('-------------\n')
    for loc in counter_loc:
        for char in counter_char:
            if counter_loc[loc] >= min_iteration  and counter_char[char] < min_iteration and have_common_word(loc, char):
                print("----")
                print('Locations : '+loc+' : '+str(counter_loc[loc]))
                print('Perso : '+char+' : '+str(counter_char[char]))
                print("----")
                
                letter_count = 0
                for c in char:
                    if c.isalpha():
                        letter_count += 1
                
                if letter_count > 2:
                        
                    for line in linesLocations:
                        if get_text(line) == loc:
                            file.write(line)
                            
                    for line in linesChar:
                        if get_text(line) == char:
                            file.write(line)
            
                