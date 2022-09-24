# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

is_continue = True
while is_continue:
    name = input("Your Name : ").upper().strip()
    try:
        nato_list = [nato_dict[letter] for letter in name]
        print(nato_list)
    except KeyError:
        print("Sorry, only letters in alphabetic please")
    else:
        is_continue = False
# name_list = [letter for letter in name]
# nato_list = [code for letter in name_list for (alpha, code) in nato_dict.items() if letter == alpha]

