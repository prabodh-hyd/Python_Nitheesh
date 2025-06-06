def rotate(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_base + key) % 26 + ascii_base
            result += chr(shifted)
        else:
            result += char
    return result
