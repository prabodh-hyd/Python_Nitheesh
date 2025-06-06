def square_root(number):
    if number == 0 or number == 1:
        return number

    left, right = 1, number // 2

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == number:
            return mid
        elif square < number:
            left = mid + 1
        else:
            right = mid - 1
    return right
pass
