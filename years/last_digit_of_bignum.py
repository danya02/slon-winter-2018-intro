#!/usr/bin/python3

def get_last_digits_of_bignum(base:int, power:int, digitcount:int) -> str:
    """
    Pessimized algorithm for getting the last digits of a bignum.
    :param base: base of exponent.
    :param power: power of exponent.
    :param digitcount: how many digits to return.
    :return: str containing the last digits.
    """
    n = 1
    for i in range(power):
        n = n * base
    n = str(n)
    return n[-digitcount:]


if __name__ == '__main__':
    print(get_last_digits_of_bignum(int(input()), int(input()), int(input())))
