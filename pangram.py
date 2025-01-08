def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence_letters = set(char.lower() for char in sentence if char.isalpha())
    return alphabet.issubset(sentence_letters)
