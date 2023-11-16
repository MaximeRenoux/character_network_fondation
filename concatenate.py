book1 = []
book2 = []

for i in range(18):
    book1.append('corpus_asimov_leaderboard/les_cavernes_d_acier/chapter_'+str(i+1)+'.txt')

for i in range(19):
    book2.append('corpus_asimov_leaderboard/prelude_a_fondation/chapter_'+str(i+1)+'.txt')

output_file_path = 'corpus_asimov_leaderboard/les_cavernes_d_acier/les_cavernes_d_acier.txt'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for chapter in book1:
        with open(chapter, 'r', encoding='utf-8') as input_file:
            output_file.write(input_file.read())
            
output_file_path = 'corpus_asimov_leaderboard/prelude_a_fondation/prelude_a_fondation.txt'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for chapter in book2:
        with open(chapter, 'r', encoding='utf-8') as input_file:
            output_file.write(input_file.read())

print("Concatenation complete.")
