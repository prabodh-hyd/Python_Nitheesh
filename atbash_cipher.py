def encode(plain_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reverse_alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    atbash = dict(zip(alphabet, reverse_alphabet))

    result = ''
    for char in plain_text.lower():
        if char.isalpha():
            result += atbash[char]
        elif char.isdigit():
            result += char

    return ' '.join(result[i:i + 5] for i in range(0, len(result), 5))


def decode(ciphered_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reverse_alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    atbash = dict(zip(alphabet, reverse_alphabet))

    result = ''
    for char in ciphered_text.lower():
        if char.isalpha():
            result += atbash[char]
        elif char.isdigit():
            result += char

    return result