import networkx as nx
import pandas as pd
import os
import re
import matplotlib.pyplot as plt

output_directory = './'
os.makedirs(output_directory, exist_ok=True)

end = '.txt.preprocessed-cleaned'
CHAPTER_NUMBER = 1

df_dict = {"ID": [], "graphml": []}

for z in range(2):
    
    if z == 0:
        BOOK = 'paf'
    else:
        BOOK = 'lca'

    if BOOK == 'lca':
        PATH = 'corpus_leaderboard/les_cavernes_d_acier/'
        book = 'les_cavernes_d_acier'
        nb_of_chapters = 18
    else:
        if BOOK == 'paf': 
            PATH = 'corpus_leaderboard/prelude_a_fondation/'
            book = 'prelude_a_fondation'
            nb_of_chapters = 19
        else: 
            print('ERROR')

    for chapter_number in range(1, nb_of_chapters+1):
        G = nx.Graph()
        CHAPTER = PATH+'chapter_'+str(chapter_number)+'.txt.preprocessed-cleaned'

        #Fetch aliases from CHARACTERS_FINAL file
        with open(PATH+book+'.txt_CHARACTERS_FINAL', 'r') as file:
            lines = file.readlines()
            
        aliasesList = []
        for line in lines:
            strings = line.strip('[]\n').split(', ')
            aliasesList.append(strings)
            
        for array in aliasesList:
            longest_string = max(array, key=len)

        window_size = len(longest_string)

        #Remove empty aliases and unwanted spaces/special characters
        temp = []
        for character in aliasesList:
            non_empty_aliases = [alias for alias in character if alias != '']
            temp.append(non_empty_aliases)
        aliasesList = temp
        
        pattern = re.compile('[^a-zA-ZÀ-ÖØ-öø-ÿ ]')
        
        for character in aliasesList:
            for i, alias in enumerate(character):
                if alias[-1] == ' ':
                    # Update the element in aliasesList
                    character[i] = alias[0:-1]
                    
        modified_aliasesList = []
        for character in aliasesList:
            modified_character = []  # New list to store modified aliases for each character
            for alias in character:
                modified_alias = pattern.sub('', alias)
                if modified_alias and modified_alias[-1] == ' ':
                    modified_alias = modified_alias[:-1]
                modified_character.append(modified_alias)
            modified_aliasesList.append(modified_character)
                    
        aliasesList = modified_aliasesList
        
        # print(aliasesList)
        # print('\n')
        
        #Initialize dictionnary of positions
        position_dict = {}

        for character in aliasesList:
            if len(character) > 0:
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
                            
                            #Avoid counting the same alias several times
                            for i in range(len(alias)):
                                buffer.pop(0)
                                buffer.append(char)
                            window = ''.join(buffer)
                            position += len(alias)
                            

        connections = {}
                            
        #Extract graph
        for key, list in position_dict.items():
            connections[key] = {}
            for key2, list2 in position_dict.items():
                for tuple in list: 
                    for tuple2 in list2:
                        if tuple2[0] - tuple[1] <= 25 and key != key2:
                            connections[key][key2] = connections[key].get(key2, 0) + 1
                    
        # print(connections)
        # print('\n\n')

        # Crée implicitement deux noeuds ("Hari" et "Dors"),
        # et ajoute un lien entre eux.
        
        for key in position_dict:
            G.add_node(key)

        for key in position_dict:
            for key2 in position_dict:
                if key != key2:
                    if key2 in connections[key]:
                        #print('creating node : '+key+' '+key2)
                        G.add_edge(key, key2)
                        
        #print(G)
                
        for node_id in G.nodes:
            G.nodes[node_id]["names"] = ""
            # print('node : ',node_id)

        for list in aliasesList:
            first = True
            for element in list:
                if first:
                    # print('liste : ',list)
                    G.nodes[list[0]]["names"] += element
                else: 
                    G.nodes[list[0]]["names"] += ';'+element
                first = False

        # print(BOOK)
        # print(chapter_number-1)
        df_dict["ID"].append("{}{}".format(BOOK, chapter_number-1))

        graphml = "".join(nx.generate_graphml(G))
        df_dict["graphml"].append(graphml)
        
        graphml_filename = os.path.join(output_directory, BOOK + '_chapter_' + str(chapter_number) + '.graphml')

        # Generate the GraphML file
        nx.write_graphml(G, graphml_filename)

        # Update the DataFrame (if needed)
        df_dict = {"ID": ["{}{}".format(BOOK+str(chapter_number-1), chapter)], "graphml": [graphml_filename]}
        df = pd.DataFrame(df_dict)
        df.set_index("ID", inplace=True)
        df.to_csv(os.path.join(output_directory, 'my_submission.csv'), mode='a', header=not os.path.exists(os.path.join(output_directory, 'my_submission.csv')))

        #Display graph
        
        # Loop through each graph and display it
        for i, (graphml_id, graphml_filename) in enumerate(zip(df_dict["ID"], df_dict["graphml"])):
            # Read the graph from the GraphML file
            G = nx.read_graphml(graphml_filename)

            # Display the graph using Matplotlib
            plt.figure(figsize=(10, 8))
            pos = nx.spring_layout(G)  # You can use a different layout algorithm if needed
            nx.draw(G, pos, with_labels=True, node_size=500, font_size=8)
            plt.title(f"Graph {i + 1}: {graphml_id}")
            plt.show()

df = pd.DataFrame(df_dict)
df.set_index("ID", inplace=True)
df.to_csv("./my_submission.csv")



        