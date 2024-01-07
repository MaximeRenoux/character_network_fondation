import re
import spacy

nlp = spacy.load("fr_core_news_lg")
alias_dict = {}

cavernes = 'corpus_leaderboard/les_cavernes_d_acier/les_cavernes_d_acier.txt'
prelude = 'corpus_leaderboard/prelude_a_fondation/prelude_a_fondation.txt'
fondation_et_empire = 'Corpus_ASIMOV/Fondation_et_empire_sample-cleaned'

FILE = cavernes

THRESHOLD = 14

def get_text(input_string):
    match = re.search(r'^\D+', input_string)
    if match:
        return match.group()
    else:
        return None

with open(FILE+"_CHARACTERS", 'r') as file:
    lines = file.readlines()
    
char_file_copy = ''

for line in lines:
    char_file_copy += ' '+line+' '
    
doc = nlp(char_file_copy)

def is_common_noun(word_to_check):
    common = False
    with open("dico_noms_communs.txt", 'r') as dico:
        dico_lines = dico.readlines()
        
    for line in dico_lines:
        for word in line.split():
            letters_only = re.sub(r'[^a-zA-ZÀ-ÖØ-öø-ÿ]', '', word)
            if word_to_check.lower() == letters_only.lower():
                common = True
    # if common:
    #     print(word_to_check)
    return common


"""Creating first dictionnary of aliases"""
for line in lines:
    bool = False

    if get_text(line) not in alias_dict:
        #print('line : ', line)
        for word_from_line in line.split():
            if len(word_from_line) >= 3:
                #print('word_from_line : ', word_from_line)
                for alias in alias_dict:
                    #print('alias : ', alias)
                    for word_from_dict in alias.split():
                        #print('word_from_dict', word_from_dict)
                        if word_from_line == word_from_dict and word_from_line.isalpha() and not is_common_noun(word_from_dict):
                            if get_text(line) not in alias_dict[alias]:
                                alias_dict[alias].append(get_text(line))
                            bool = True
                        
    if bool == False:
        alias_dict[get_text(line)] = []
        
print(alias_dict)
        
"""Merging errors"""
merged_dict = {}

for key, values in alias_dict.items():
    merged = False
    
    # Check if the values share a common word with any other key
    for merged_key, merged_values in merged_dict.items():
        if any(word in merged_values for word in values):
            merged_values.extend(values)
            merged = True
            break
    
    # If no common word is found, add the key to the merged dictionary
    if not merged:
        merged_dict[key] = values

# # Print the merged dictionary
# for key, values in merged_dict.items():
#     print(f"key {key}: {values}")
    
    
"""Writing aliases with enough occurences in CHARACTERS_FINAL"""
counter_dict = {}    

for key in merged_dict:
    counter_dict[key] = 0

for key, values in merged_dict.items():
    
    for line in lines:
        if get_text(line) == key:
            counter_dict[key] += 1
        for value in values:
            if get_text(line) == value:
                counter_dict[key] += 1
                
# # Print the number of appearances
# for key, values in counter_dict.items():
#     print(f"key {key}: {values}")
    
final_aliases = []

for key in merged_dict:
    if counter_dict[key] > THRESHOLD:
        final_aliases.append([])
        final_aliases[-1].append(key)
        for value in merged_dict[key]:
            final_aliases[-1].append(value)
            
with open(FILE+"_CHARACTERS_FINAL", 'w', encoding='utf-8') as file:
    for alias_list in final_aliases:
        file.write('[' + ', '.join(map(str, alias_list)) + ']\n')
        
    
# modified_character_file = []
    
# for key, values in merged_dict.items():
    
#     for line in lines:
#         if get_text(line) == key and counter_dict[key] > 15:
#             modified_character_file.append(line)
#         for value in values:
#             if get_text(line) == value and counter_dict[key] > 15:
#                 modified_character_file.append(line)
                                
# with open(FILE+"_CHARACTERS_FINAL", 'w', encoding='utf-8') as file:
#     file.writelines(modified_character_file)
                
  
    