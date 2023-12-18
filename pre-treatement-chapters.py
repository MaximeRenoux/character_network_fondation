import re

chapters = []

# chapters.append('corpus_leaderboard/les_cavernes_d_acier/chapter_1.txt.preprocessed')

for i in range(18):
    chapters.append('corpus_leaderboard/les_cavernes_d_acier/chapter_'+str(i+1)+'.txt.preprocessed')

for i in range(19):
    chapters.append('corpus_leaderboard/prelude_a_fondation/chapter_'+str(i+1)+'.txt.preprocessed')
    
for file_path in chapters:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    pagination1 = re.compile(r'�\d+�')
    pagination2 = re.compile(r'�\s*\d+\s*�')
    pagination3 = re.compile(r'-\d+-')
    pagination4 = re.compile(r'-\s*\d+\s*-')
    pagination5 = re.compile(r'\b\d+\b\n')
    pattern_roman = re.compile(r'\b(?:I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV|XVI|XVII|XVIII|XIX|XX)\b\n')

    # Remove pagination
    with open(file_path + '-cleaned', 'w', encoding='utf-8') as cleaned_file:
        for line in lines:
            if pagination1.match(line) or pagination2.match(line) or pattern_roman.match(line) or pagination3.match(line) or pagination4.match(line) or pagination5.match(line):
                print(line)
            if not pagination1.match(line) and not pagination2.match(line) and not pattern_roman.match(line) and not pagination3.match(line) and not pagination4.match(line) and not pagination5.match(line):
                cleaned_file.write(line)

    with open(file_path + '-cleaned', 'r', encoding='utf-8') as cleaned_file: 
        content = cleaned_file.read()

    # Remove unnecessary \n
    modified_content = re.sub(r'([a-zàâçéèêëîïôûùüÿñ])\n([a-zàâçéèêëîïôûùüÿñ])|([A-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÑ])\n([a-zàâçéèêëîïôûùüÿñ])', r'\1 \2 \3 \4', content)
    modified_content = re.sub(r'([a-zA-Zàâçéèêëîïôûùüÿñ])  ', r'\1', modified_content)
    modified_content = modified_content.replace('\n\n\n', '\n')
    modified_content = modified_content.replace('II', 'Il')

    with open(file_path + '-cleaned', 'w', encoding='utf-8') as cleaned_file:
        cleaned_file.write(modified_content)

    print("Process complete.")
