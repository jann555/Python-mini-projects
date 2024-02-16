import pandas as pd

data = pd.read_csv('../../resources/nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

nato = [phonetic_dict[letter] for letter in word]

print(nato)
