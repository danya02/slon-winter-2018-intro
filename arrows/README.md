# TL;DR: [this script](solution_curses.py), or [this one](solution_pygame.py), or [this](solution_pygame_complex.py)
AKA "There's More Than One Way to Do It".

This is pretty simple to do, but can be made arbitrarily complex.
The [`curses` implementation](solution_curses.py) does this the most simple way I could think of.

A [`pygame` implementation](solution_pygame.py) is also available.
It does this almost exactly the same way as the `curses` version, sans the magic inherent in `curses`.
And since it works almost exactly like the `curses` version, it's boring.
And since it's boring, one has to question why anyone would want to play this as-is.

And it is because it is boring that I have made a [better `pygame` version](pygame_solution_complex.py).
It has some bugs related to keyboard input, but does reliably work with inputs of one key at a time.

However, I cannot tell you anything about it.
**Its very nature is shrouded in darkness**.
Ha ha ha.
