def is_isogram(string):
    characters = "".join(char.lower() for char in string if char.isalpha())
    return len(characters) == len(set(characters))


