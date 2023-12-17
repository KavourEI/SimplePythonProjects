import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word:").upper()
    try:
        word_nato = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters of the alphabet please")
        generate_phonetic()
    else:
        print(word_nato)

generate_phonetic()




