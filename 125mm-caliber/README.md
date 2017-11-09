# TL,DR: [this script](solution.py)
AKA "Revenge of the Linguists".

(Idea partially taken from [this](https://github.com/seriyps/ru_number_to_text) project, which implements this task way better than this.)

The `split_int` function is internal and you should not be using it.
The `get_string_of_int` function returns a string representation of a number up to 1000, for example: `сто двадцать пять`.
The `get_string_of_big_int` function returns a string representation for numbers in range(-999999999999, 1000000000000).
The maximum value that it is possible to get is `девятьсот девяносто девять миллиардов девятьсот девяносто девять миллионов девятьсот девяносто девять тысяч девятьсот девяносто девять`. 