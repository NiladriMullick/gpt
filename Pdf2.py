import nltk
from nltk.corpus import wordnet

def get_verb_variations(word):
    variations = set()
    for synset in wordnet.synsets(word, pos='v'):
        for lemma in synset.lemmas():
            variations.add(lemma.name())
    return variations

words = ["play", "eat", "run"]  # Example list of words
verb_variations = {}
for word in words:
    verb_variations[word] = get_verb_variations(word)

print("Verb Variations:")
for word, variations in verb_variations.items():
    print(f"{word}: {', '.join(variations)}")
