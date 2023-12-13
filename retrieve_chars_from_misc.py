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
    
def have_common_word(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())
    
    common_words = words1.intersection(words2)
    
    return len(common_words) > 0
    
counter_char = {}
counter_misc = {}
min_iteration = 3


with open(BOOK+'_characters.txt', 'r', encoding='utf-8') as file:
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
        
with open(BOOK+'_misc.txt', 'r', encoding='utf-8') as file:
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

with open(BOOK+'_misc.txt', 'r', encoding='utf-8') as originalMiscFile:
    linesMisc = originalMiscFile.readlines()
with open(BOOK+'_characters.txt', 'r', encoding='utf-8') as originalCharFile:
    linesChar = originalCharFile.readlines()
    


with open(BOOK+'_characters.txt', 'a', encoding='utf-8') as file:
    file.write('--------------------')
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
                
                if letter_count > 2:
                        
                    for line in linesMisc:
                        if get_text(line) == misc:
                            file.write(line)
                            
                    for line in linesChar:
                        if get_text(line) == char:
                            file.write(line)
            
# with open(BOOK+'lost_characters.txt', 'a', encoding='utf-8') as file:
#     file.write('--------------------')
#     for error in counter_misc:
#         print(counter_char[error])
        
                