#!/usr/bin/python3
import textwrap


def get_optimum_orientation(text: str) -> int:
    """
    Get an optimum orientation to print a text.
    Take a string containing the text to print.
    If it takes less pages to print it vertically, return -1; if horizontally, return 1; if it doesn't matter, return 0.
    """
    for i in text.split():
        if len(i) > 20:
            raise ValueError("word length exceeds max line length ({}>20)".format(len(i)))
        if 15 < len(i) < 20:
            return -1
    ver_wrap = textwrap.wrap(text, 15)
    ver_wrap = [ver_wrap[i:i + 20] for i in range(0, len(ver_wrap), 20)]
    hor_wrap = textwrap.wrap(text, 20)
    hor_wrap = [hor_wrap[i:i + 15] for i in range(0, len(hor_wrap), 15)]
    print(len(ver_wrap), len(hor_wrap))
    if len(ver_wrap) == len(hor_wrap):
        return 0
    elif len(ver_wrap) > len(hor_wrap):
        return 1
    elif len(ver_wrap) < len(hor_wrap):
        return -1
    raise EnvironmentError("logic is confirmed to be broken")


if __name__ == '__main__':
    print(["|", "=", "-"][get_optimum_orientation(input()) + 1])
