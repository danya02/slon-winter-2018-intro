#!/usr/bin/python3
import sys


def split_int(n: int) -> (bool, (int, int, int, int)):
    """
    Split the given int into pieces of 3 registers.
    """
    if abs(n) > 999999999999:
        raise OverflowError('number too large or too small')
    if not isinstance(n, int):
        raise TypeError('number must be integer')
    sign = n < 0
    n = abs(n)
    return sign, tuple([int(i) for i in [str(n).rjust(12, "0")[i:i + 3] for i in range(0, 12, 3)]])


def get_string_of_int(n: int, gender: bool = True) -> str:
    """
    Get a stringified version of an int in range(0, 1000).
    gender is optional and is True for masculine, False for feminine.
    Raise an OverflowError if the number is not in that range.
    """
    if n in range(20):
        return \
            ["нуль", "один" if gender else "одна", "два" if gender else "две", "три", "четыре", "пять", "шесть", "семь",
             "восемь", "девять", "десять",
             "одиннадцать",
             "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать",
             "девятнадцать"][n]
    if n in range(20, 100):
        n0 = n % 10
        n1 = n // 10
        output=[]
        output += [["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
              "девяносто"][n1]]
        output += [(["", "один" if gender else "одна", "два" if gender else "две", "три", "четыре", "пять", "шесть",
           "семь",
           "восемь", "девять"][n0])]
        return " ".join(output).strip()
    if n in range(100, 1000):
        n0 = n % 10
        n1 = n // 10 % 10
        n2 = n // 100
        output = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот",
                  "девятьсот"][n2]
        output += (" " + get_string_of_int(n1 * 10 + n0, gender)) if n1 + n0 > 0 else ""
        return "".join(output).strip()
    raise OverflowError("{} not in range(0, 1000).".format(n))


def get_string_of_big_int(n: int, forms: ((str, str, str), bool) = (("", "", ""), True)):
    """
    Get a stringified version of an int in range(-999999999999, 1000000000000).
    forms should be ((str_for_1, str_for_2_to_4, str_for_else), gender), and is empty strings and masculine by default.
    Raises an OverflowError if the int is not in the range.
    """
    oom = [forms,
           ((u'тысяча', u'тысячи', u'тысяч'), False),
           ((u'миллион', u'миллиона', u'миллионов'), True),
           ((u'миллиард', u'миллиарда', u'миллиардов'), True)]
    oom.reverse()
    sign, num = split_int(n)
    output = "минус " if sign else ""
    for i, j in zip(oom, num):
        if j:
            ind = j % 100
            output += get_string_of_int(j, i[1]) + " " + i[0][
                ([2, 0] + [1] * 3 + [2] * 15 + [2, 0, 1, 1, 1, 2, 2, 2, 2, 2] * 8)[ind]] + " "
    if output == "минус " or output == "":
        output += "нуль " + forms[0][2]
    elif j==0:
        output += forms[0][2]
    return output.strip()


if __name__ == '__main__':
    print("калибр:", get_string_of_big_int(125 if len(sys.argv)==1 else int(sys.argv[1]), (("миллиметр", "миллиметра", "миллиметров"), True)))
