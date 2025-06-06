def is_paired(input_string):
    chars = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in '({[':
        if char in brackets:
            chars.append(char)
        elif char in ')}]':
            if not chars or chars.pop() != brackets[char]:
                return False
    return len(chars) == 0
pass
