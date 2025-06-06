def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    total = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        total += int(isbn[i]) * (10 - i)
    check = isbn[9]
    if check == 'X':
        total += 10
    elif check.isdigit():
        total += int(check)
    else:
        return False
    return total % 11 == 0
