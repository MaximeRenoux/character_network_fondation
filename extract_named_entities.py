import spacy
# from thinc.api import set_gpu_allocator, require_gpu
# set_gpu_allocator("pytorch")
# require_gpu(0)

# nlp = spacy.load("fr_dep_news_trf", disable=["parser", "tagger"])

nlp = spacy.load("fr_core_news_lg")

with open('asimov.txt', 'r', encoding='utf-8') as book: 
    text = book.read()
    doc = nlp(text)

with open('characters_trf.txt', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'PER':
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.label_)+"\n")

with open('locations_trf.txt', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'LOC':
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.label_)+"\n")
            
with open('misc_trf.txt', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'MISC':
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.label_)+"\n")
            
with open('organizations_trf.txt', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'ORG':
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.label_)+"\n")
