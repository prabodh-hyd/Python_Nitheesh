def answer(question):
    question = question.replace("What is", "").strip().rstrip("?").strip()
    if not question:
        raise ValueError("syntax error")

    tokens = question.split()
    if len(tokens) == 1:
        try:
            return int(tokens[0])
        except ValueError:
            raise ValueError("syntax error")

    equation = []
    i = 0
    expect_number = True
    while i < len(tokens):
        if expect_number:
            try:
                equation.append(int(tokens[i]))
                i += 1
                expect_number = False
            except ValueError:
                raise ValueError("syntax error")
        else:
            if (i + 1 < len(tokens) and
                    tokens[i] in ["multiplied", "divided"] and
                    tokens[i + 1] == "by"):
                operation = tokens[i]
                i += 2
            else:
                operation = tokens[i]
                i += 1

            if operation in ["plus", "minus", "multiplied", "divided"]:
                equation.append(operation)
                expect_number = True
            else:
                is_number = True
                try:
                    int(operation)
                except ValueError:
                    is_number = False
                if is_number:
                    raise ValueError("syntax error")
                else:
                    raise ValueError("unknown operation")

    if len(equation) % 2 == 0 or not equation:
        raise ValueError("syntax error")

    result = equation[0]
    for i in range(1, len(equation), 2):
        operation = equation[i]
        number = equation[i + 1]
        if operation == "plus":
            result += number
        elif operation == "minus":
            result -= number
        elif operation == "multiplied":
            result *= number
        elif operation == "divided":
            if number == 0:
                raise ValueError("syntax error")
            result //= number
    return result