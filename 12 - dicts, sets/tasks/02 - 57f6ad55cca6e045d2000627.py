def square_or_square_root(numbers):
    result = []
    for number in numbers:
        sq_root = number ** 0.5
        if sq_root.is_integer():
            result.append(int(sq_root))
        else:
            result.append(number ** 2)
    return result


def square_or_square_root(numbers):
    result = []
    for number in numbers:
        if (sq_root := number ** 0.5).is_integer():
            result.append(int(sq_root))
        else:
            result.append(number ** 2)
    return result


assert square_or_square_root([4, 3, 9, 7, 2, 1]) == [2, 9, 3, 49, 4, 1]
assert square_or_square_root([100, 101, 5, 5, 1, 1]) == [10, 10201, 25, 25, 1, 1]
assert square_or_square_root([1, 2, 3, 4, 5, 6]) == [1, 4, 9, 2, 25, 36]
