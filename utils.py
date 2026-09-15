def reversed(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    return int(str(number)[::-1])


def formatter(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    return bin(number), oct(number)