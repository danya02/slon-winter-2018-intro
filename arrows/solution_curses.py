#!/usr/bin/python3
import curses

# Modify these to suit your needs.
width = 10
height = 10
screen = None
pos = [4, 4]


def init() -> None:
    """
    Initialize the screen and colors.
    """
    global screen
    screen = curses.initscr()
    curses.curs_set(0)
    screen.keypad(1)
    curses.start_color()
    curses.init_pair(10, curses.COLOR_WHITE, curses.COLOR_BLACK)  # empty space color
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)  # chara color
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)  # top border color
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_GREEN)  # bottom border color
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)  # left border color
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)  # right border color
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_GREEN)  # top-left corner color
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_GREEN)  # top-right corner color
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_GREEN)  # bottom-left corner color
    curses.init_pair(9, curses.COLOR_WHITE, curses.COLOR_GREEN)  # bottom-right corner color


def draw() -> None:
    """
    Update the screen.

    Since it's pretty cheap, this redraws the entire screen.
    However, this may cause problems on some terminal.
    Those of you who still use 300-baud terminals, AVOID.
    (Better yet, upgrade to the 21, 20 or 19 century and get a TTY emulator.)
    """
    screen.addstr(0, 0, chr(0x2500) * (width + 2), curses.color_pair(2))
    screen.addstr(height + 1, 0, chr(0x2500) * (width + 2), curses.color_pair(3))
    for i in range(height + 2):
        screen.addstr(i, 0, chr(0x2502), curses.color_pair(4))
        screen.addstr(i, width + 1, chr(0x2502), curses.color_pair(5))
    screen.addstr(0, 0, chr(0x250c), curses.color_pair(6))
    screen.addstr(height + 1, 0, chr(0x2514), curses.color_pair(7))
    screen.addstr(0, width + 1, chr(0x2510), curses.color_pair(8))
    screen.addstr(height + 1, width + 1, chr(0x2518), curses.color_pair(9))

    for i in range(height):
        screen.addstr(i + 1, 1, "." * width, curses.color_pair(10))
    screen.addstr(pos[1] + 1, pos[0] + 1, "@", curses.color_pair(1))
    screen.refresh()


def move(point: int) -> None:
    """
    Move one cell in given direction.
    direction is 0 for up, 1 for left, 2 for down and 3 for right.
    """
    global pos
    if point == 3:
        pos = [pos[0] + 1, pos[1]]
        if pos[0] > width - 1:
            pos[0] = 0
    elif point == 2:
        pos = [pos[0], pos[1] + 1]
        if pos[1] > height - 1:
            pos[1] = 0
    elif point == 1:
        pos = [pos[0] - 1, pos[1]]
        if pos[0] < 0:
            pos[0] = width - 1
    elif point == 0:
        pos = [pos[0], pos[1] - 1]
        if pos[1] < 0:
            pos[1] = height - 1
    else:
        raise ValueError("direction must be in range(0, 4).")


def mainloop() -> None:
    """
    Run the program.
    """
    init()
    run = True
    while run:
        b = screen.getch()
        if b == ord('q') or b == curses.KEY_BREAK or b == curses.KEY_EXIT:
            curses.endwin()
            run = False
        elif b == curses.KEY_UP:
            move(0)
        elif b == curses.KEY_LEFT:
            move(1)
        elif b == curses.KEY_DOWN:
            move(2)
        elif b == curses.KEY_RIGHT:
            move(3)
        draw()


if __name__ == '__main__':
    mainloop()
