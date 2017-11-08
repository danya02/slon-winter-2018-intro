# TL,DR: [this script](solution.py)
AKA "Monospace Fonts are a Good Thing".

This one is pretty straightforward.
[This](solution.py) file contains a `get_optimum_orientation(str) -> int` function.

First, check if the input is sane; that is, if words are not longer than 20 chars.
If there are any words longer than 15 chars, return now; we can't break words.
Then, wrap the lines using, appropriately enough, `textwrap.wrap`.
Then split the result by 15 and 20 lines and compare length.

If it takes less pages to print the text vertically, it will return -1; if horizontally, it will return 1; if it doesn't matter, it will return 0.
