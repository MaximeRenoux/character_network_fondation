import spacy
import re
# from thinc.api import set_gpu_allocator, require_gpu
# set_gpu_allocator("pytorch")
# require_gpu(0)

# nlp = spacy.load("fr_dep_news_trf", disable=["parser", "tagger"])

cavernes = 'corpus_leaderboard/les_cavernes_d_acier/les_cavernes_d_acier.txt'
prelude = 'corpus_leaderboard/prelude_a_fondation/prelude_a_fondation.txt'
fondation_et_empire = 'Corpus_ASIMOV/Fondation_et_empire_sample-cleaned'

BOOK = cavernes

nlp = spacy.load("fr_core_news_lg")

with open(BOOK, 'r', encoding='utf-8') as book: 
    text = book.read()
    doc = nlp(text)

with open(BOOK+'_CHARACTERS', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'PER' and re.search(r'[A-Z]', str(ent.text)) and (ent.root.pos_ == "PROPN" or ent.root.pos_ == "NOUN"):
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.root.pos_)+" "+str(ent.label_)+"\n")

with open(BOOK+'_LOCATIONS', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'LOC' and re.search(r'[A-Z]', str(ent.text)) and (ent.root.pos_ == "PROPN" or ent.root.pos_ == "NOUN"):
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.root.pos_)+" "+str(ent.label_)+"\n")
            
with open(BOOK+'_MISC', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'MISC' and re.search(r'[A-Z]', str(ent.text)) and (ent.root.pos_ == "PROPN" or ent.root.pos_ == "NOUN"):
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.root.pos_)+" "+str(ent.label_)+"\n")
            
with open(BOOK+'_ORGANIZATIONS', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'ORG'  and re.search(r'[A-Z]', str(ent.text)) and (ent.root.pos_ == "PROPN" or ent.root.pos_ == "NOUN"):
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.root.pos_)+" "+str(ent.label_)+"\n")
