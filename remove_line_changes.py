import re

for i in range(18):
    with open('corpus_asimov_leaderboard/les_cavernes_d_acier/chapter_'+str(i+1)+'.txt.preprocessed', 'r', encoding='utf-8') as chapter:
        content = chapter.read()
        
    modified_content = re.sub(r'([a-zA-Z])\n([a-zA-Z])', ' ', content)
    modified_content = modified_content.replace('\n\n\n', '\n')
    
    with open('corpus_asimov_leaderboard/les_cavernes_d_acier/chapter_'+str(i+1)+'.txt', 'w', encoding='utf-8') as file:
        file.write(modified_content)
        
    print('Chapter '+str(i+1)+' done!')
    
print('Finished!')

for i in range(19):
    with open('corpus_asimov_leaderboard/prelude_a_fondation/chapter_'+str(i+1)+'.txt.preprocessed', 'r', encoding='utf-8') as chapter:
        content = chapter.read()
        
    modified_content = re.sub(r'([a-zA-Z])\n([a-zA-Z])', ' ', content)
    modified_content = modified_content.replace('\n\n\n', '\n')
    
    with open('corpus_asimov_leaderboard/prelude_a_fondation/chapter_'+str(i+1)+'.txt', 'w', encoding='utf-8') as file:
        file.write(modified_content)
        
    print('Chapter '+str(i+1)+' done!')
    
print('Finished!')
    