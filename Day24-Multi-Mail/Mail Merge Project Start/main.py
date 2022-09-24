# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt

# ./ for current dir ../ to move upward in the dir tree
with open('./Input/Names/invited_names.txt') as file:
    names = file.read().split("\n")

for name in names:
    with open('./Input/Letters/starting_letter.txt') as infile:
        letter_content = infile.read().replace('[name]', name)

    with open(f'./Output/ReadyToSend/readytosendto{name}.txt', mode='w') as opfile:
        opfile.write(letter_content)

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp