def is_armstrong_number(number):
    digits = str(number)
    length_n = len(digits)
    armstrong_number = sum(int(i) ** length_n for i in digits)
    return armstrong_number == number
