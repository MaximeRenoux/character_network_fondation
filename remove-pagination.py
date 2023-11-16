# print('Enter file name:')
# file_path = input()

file_path = "Fondation_sample.txt"

# Read the content of the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove pagination lines
for line in lines:
    line=line.decode('utf-8','ignore').encode("utf-8")

# Write the modified content back to the file
with open("sample-new.txt", 'w') as file:
    file.writelines(lines)

print("Pagination removed.")