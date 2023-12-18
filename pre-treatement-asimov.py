import re

file_path = 'Corpus_ASIMOV/Fondation_sample'
file_path2 = 'Corpus_ASIMOV/Fondation_et_empire_sample'
file_path3 = 'Corpus_ASIMOV/Fondation_foudroyée_sample'
file_path4 = 'Corpus_ASIMOV/Seconde_Fondation_sample'
file_path5 = 'Corpus_ASIMOV/Terre_et_Fondation_sample'

FILE = 'corpus_leaderboard/les_cavernes_d_acier/chapter_1.txt.preprocessed'

with open(FILE, 'r', encoding='utf-8') as file:
    lines = file.readlines()

pagination1 = re.compile(r'�\d+�')
pagination2 = re.compile(r'�\s*\d+\s*�')
pagination3 = re.compile(r'-\d+-')
pagination4 = re.compile(r'-\s*\d+\s*-')
pagination5 = re.compile(r'\b\d+\b\n')
pattern_roman = re.compile(r'\b(?:I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV|XVI|XVII|XVIII|XIX|XX)\b\n')

# Remove pagination
with open(FILE + '-cleaned', 'w', encoding='utf-8') as file:
    for line in lines:
        if pagination1.match(line) or pagination2.match(line) or pattern_roman.match(line) or pagination3.match(line) or pagination4.match(line) or pagination5.match(line):
            print(line)
        if not pagination1.match(line) and not pagination2.match(line) and not pattern_roman.match(line) and not pagination3.match(line) and not pagination4.match(line) and not pagination5.match(line):
            file.write(line)

with open(FILE + '-cleaned', 'r', encoding='utf-8') as file: 
    content = file.read()

# Remove unnecessary \n
modified_content = re.sub(r'([a-z])\n([a-z])|([A-Z])\n([a-z])', r'\1\2\3\4', content)
modified_content = modified_content.replace('\n\n\n', '\n')
modified_content = modified_content.replace('II', 'Il')

with open(FILE + '-cleaned', 'w', encoding='utf-8') as file:
    file.write(modified_content)

print("Process complete.")
