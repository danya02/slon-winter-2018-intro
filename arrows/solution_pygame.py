#!/usr/bin/python3
import pygame

# Modify these to suit your needs.
width = 10
height = 10
scale = 32
screen = None
virtual_screen = None
pos = [4, 4]


def init() -> None:
    """
    Initialize the surfaces.
    """
    global screen
    global virtual_screen
    virtual_screen = pygame.Surface((width, height))
    screen = pygame.display.set_mode((width * scale, height * scale))


def draw() -> None:
    """
    Update the surface. (And the physical surface too.)
    """
    virtual_screen.fill(pygame.Color('black'))
    virtual_screen.set_at(pos, pygame.Color('red'))
    pygame.transform.scale(virtual_screen, (width * scale, height * scale), screen)
    pygame.display.flip()


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_ESCAPE, pygame.K_BREAK, pygame.K_q]:
                    pygame.quit()
                    exit(0)
                elif event.key == pygame.K_UP:
                    move(0)
                elif event.key == pygame.K_LEFT:
                    move(1)
                elif event.key == pygame.K_DOWN:
                    move(2)
                elif event.key == pygame.K_RIGHT:
                    move(3)
                draw()


if __name__ == '__main__':
    mainloop()
