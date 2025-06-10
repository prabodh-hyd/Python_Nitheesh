def annotate(minefield):
    if not isinstance(minefield, list) or not all(isinstance(row, str) for row in minefield):
        raise ValueError("The board is invalid with current input.")
    elif not minefield:
        return []
    elif not all(len(row) == len(minefield[0]) for row in minefield):
        raise ValueError("The board is invalid with current input.")
    elif not all(all(char in ' *' for char in row) for row in minefield):
        raise ValueError("The board is invalid with current input.")

    rows = len(minefield)
    columns = len(minefield[0])
    result = []

    for i in range(rows):
        row_list = []
        for j in range(columns):
            if minefield[i][j] == "*":
                row_list.append('*')
            else:
                count = 0
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if k != 0 or l != 0:
                            ni = i + k
                            nj = j + l
                            if 0 <= ni < rows and 0 <= nj < columns and minefield[ni][nj] == "*":
                                count += 1
                row_list.append(' ' if count == 0 else str(count))
        result.append(''.join(row_list))
    return result