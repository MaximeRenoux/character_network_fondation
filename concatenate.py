file_paths = [
    'Corpus_ASIMOV/Fondation_sample-cleaned.txt',
    'Corpus_ASIMOV/Fondation_et_empire_sample-cleaned.txt',
    'Corpus_ASIMOV/Fondation_foudroyée_sample-cleaned.txt',
    'Corpus_ASIMOV/Seconde_Fondation_sample-cleaned.txt',
    'Corpus_ASIMOV/Terre_et_Fondation_sample-cleaned.txt'
]

output_file_path = 'Corpus_ASIMOV/concatenated_samples.txt'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            output_file.write(input_file.read())

print("Concatenation complete.")
