def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    boolean = True
    iteration = 0
    while boolean:
        if number == 1:
            boolean = False
            break
        if number % 2 == 0:
            number //= 2
        else:
            number = (3*number) + 1
        iteration += 1
    return iteration
