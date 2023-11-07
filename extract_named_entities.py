import spacy

nlp = spacy.load("fr_core_news_md")

with open('asimov.txt', 'r', encoding='utf-8') as book: 
    text = book.read()
    doc = nlp(text)

with open('characters.txt', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'PER':
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.label_)+"\n")

with open('locations.txt', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'LOC':
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.label_)+"\n")
            
with open('misc.txt', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'MISC':
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.label_)+"\n")
            
with open('organizations.txt', 'w', encoding='utf-8') as file:
    for ent in doc.ents:
        if ent.label_ == 'ORG':
            file.write(str(ent.text)+" "+str(ent.start_char)+" "+str(ent.end_char)+" "+str(ent.label_)+"\n")
