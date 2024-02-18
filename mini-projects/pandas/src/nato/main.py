import pandas as pd

data = pd.read_csv('../../resources/nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        nato = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Only Errors in the Alphabet Please')
        generate_phonetic()
    else:
        print(nato)


generate_phonetic()
