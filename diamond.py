def rows(letter):
    if not letter.isalpha() or not letter.isupper() or len(letter) != 1:
        return None

    n = ord(letter) - ord('A')
    result = []

    for i in range(n + 1):
        char = chr(ord('A') + i)
        spaces = n - i
        if i == 0:
            row = " " * spaces + char + " " * spaces
        else:
            row = " " * spaces + char + " " * (2 * i - 1) + char + " " * spaces
        result.append(row)

    for i in range(n - 1, -1, -1):
        result.append(result[i])
    return result