import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

def tokenize_text(text):
    return word_tokenize(text)

sample_inputs = [
    "Natural Language Processing is interesting.",
    "My name is Gokul.",
    "Studing third year ADS."
]

for text in sample_inputs:
    print("Input Text:")
    print(text)
    print("Tokens:")
    print(tokenize_text(text))
    print("-" * 40)
