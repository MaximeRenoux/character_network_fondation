import networkx as nx
import pandas as pd

cav1 = 'corpus_leaderboard/les_cavernes_d_acier/chapter_1.txt.preprocessed-cleaned'

CHAPTER = cav1

#Fetch aliases from CHARACTERS_FINAL file
with open('corpus_leaderboard/les_cavernes_d_acier/les_cavernes_d_acier.txt_CHARACTERS_FINAL', 'r') as file:
    lines = file.readlines()
    
aliasesList = []
for line in lines:
    strings = line.strip('[]\n').split(', ')
    aliasesList.append(strings)
    
for array in aliasesList:
    longest_string = max(array, key=len)

window_size = len(longest_string)

#Remove empty aliases
temp = []
for character in aliasesList:
    non_empty_aliases = [alias for alias in character if alias != '']
    temp.append(non_empty_aliases)
aliasesList = temp

#Initialize dictionnary of positions
position_dict = {}

for character in aliasesList:
    position_dict[character[0]] = []

with open(CHAPTER, 'r') as chapter:
    buffer = [''] * window_size
    position = 0
    
    while True:
        char = chapter.read(1)
        if not char:
            break  # End of file
        buffer.pop(0)
        buffer.append(char)
        window = ''.join(buffer)
        
        position += 1
        
        for character in aliasesList:
            for alias in character:
                if alias in window:
                    #save start and end position
                    position_dict[character[0]].append([position, position + len(alias) - 1])

connections = {}
                    
#Extract graph
for key, list in position_dict.items():
    connections[key] = {}
    for key2, list2 in position_dict.items():
        for tuple in list: 
            for tuple2 in list2:
                print(tuple2)
                if tuple2[0] - tuple[1] <= 25 and key != key2:
                    connections[key][key2] = connections[key].get(key2, 0) + 1
            
#print(connections)

G = nx.Graph()

# Crée implicitement deux noeuds ("Hari" et "Dors"),
# et ajoute un lien entre eux.

for key in position_dict:
    for key2 in position_dict:
        G.add_edge(key, key2)

for list in aliasesList:
    # On ajoute les attributs "names"
    G.nodes[list[0]]["names"] = list

df_dict = {"ID": [], "graphml": []}
df_dict["ID"].append("{}{}".format(book_code, chapter))

graphml = "".join(nx.generate_graphml(G))
df_dict["graphml"].append(graphml)

df = pd.DataFrame(df_dict)
df.set_index("ID", inplace=True)
df.to_csv('./cavernes'+CHAPTER+'.csv')