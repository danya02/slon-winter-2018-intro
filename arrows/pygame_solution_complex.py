#!/usr/bin/python3
import pygame
import threading
import gzip

screen = None
pos = [4, 4]
pos_to = [4, 4]
pos_sprite = [0, 0]
surfaces = None
pointing = 2
moving = False
move_phase = 0.0
cycle_phase = 0
wraparound = -1
wrapped_around = True
run = True


def deep_magic(*args):
    print("""What are you doing?
Looking for secrets?
Don't put your nose where it doesn't belong.
Or you might learn something you DON'T like...
Hee hee hee.""")


magic = deep_magic


def init() -> None:
    """
    Initialize the surfaces.
    """
    global screen
    screen = pygame.display.set_mode((800, 800))
    global surfaces
    surfaces = magic()


def calc_sprite_pos():
    global pos_sprite
    if not moving:
        pos_sprite = [80 * pos[0] + 40 - int(surfaces[pointing][int(cycle_phase)].get_width() / 2),
                      80 * pos[1] + 40 - int(surfaces[pointing][int(cycle_phase)].get_height() / 2)]
    else:
        if pointing == 0:
            pos_sprite = [80 * pos[0] + 40 - int(surfaces[pointing][int(cycle_phase)].get_width() / 2),
                          80 * pos[1] + 40 - int(surfaces[pointing][int(cycle_phase)].get_height() / 2) - int(
                              move_phase * 80)]
        elif pointing == 1:
            pos_sprite = [
                80 * pos[0] + 40 - int(surfaces[pointing][int(cycle_phase)].get_width() / 2) - int(move_phase * 80),
                80 * pos[1] + 40 - int(surfaces[pointing][int(cycle_phase)].get_height() / 2)]
        elif pointing == 2:
            pos_sprite = [80 * pos[0] + 40 - int(surfaces[pointing][int(cycle_phase)].get_width() / 2),
                          80 * pos[1] + 40 - int(surfaces[pointing][int(cycle_phase)].get_height() / 2) + int(
                              move_phase * 80)]
        elif pointing == 3:
            pos_sprite = [
                80 * pos[0] + 40 - int(surfaces[pointing][int(cycle_phase)].get_width() / 2) + int(move_phase * 80),
                80 * pos[1] + 40 - int(surfaces[pointing][int(cycle_phase)].get_height() / 2)]


def drawcycle() -> None:
    """
    Update the surface. (And the physical surface too.)
    """
    global move_phase
    global cycle_phase
    global pos_to
    global pos
    global wraparound
    global wrapped_around
    global run
    clock = pygame.time.Clock()
    grid = []
    for i in range(0, 800, 80):
        for j in range(0, 800, 80):
            grid += [pygame.Rect((i, j), (80, 80))]
    while run:
        clock.tick(30)
        screen.fill(pygame.Color('black'))
        for i in grid:
            pygame.draw.rect(screen, pygame.Color('white'), i, 1)
        if moving:
            move_phase += 0.05
            if move_phase >= 1:
                pos = pos_to
                get_movement()
                move_phase = 0
                if wraparound == -1:
                    test_pressed()
                else:
                    wrapped_around += 1
                    if wrapped_around > 8:
                        run = False
                        deep_magic()
                    if wraparound == 0:
                        pos = [pos[0], -1]
                    if wraparound == 2:
                        pos = [pos[0], 10]
                    if wraparound == 3:
                        pos = [10, pos[1]]
                    if wraparound == 1:
                        pos = [-1, pos[1]]
                    wraparound = -1
            cycle_phase += 0.2
            if int(cycle_phase) >= len(surfaces[pointing]):
                cycle_phase = 0
        else:

            move_phase = 0
            cycle_phase = 0
        calc_sprite_pos()
        screen.blit(surfaces[pointing][int(cycle_phase)], tuple(pos_sprite))
        pygame.display.flip()


def move(point: int) -> None:
    """
    Move one cell in given direction.
    direction is 0 for up, 1 for left, 2 for down and 3 for right.
    """
    global pos
    global pos_to
    global pointing
    global moving
    global wraparound
    pointing = point
    if 1:
        if point == 3:
            pos_to = [pos[0] + 1, pos[1]]
            if pos_to[0] > 9:
                pos_to[0] = 0
                wraparound = 1
            moving = True
        elif point == 2:
            pos_to = [pos[0], pos[1] + 1]
            if pos_to[1] > 9:
                pos_to[1] = 0
                wraparound = 0
            moving = True
        elif point == 1:
            pos_to = [pos[0] - 1, pos[1]]
            if pos_to[0] < 0:
                pos_to[0] = 9
                wraparound = 3
            moving = True
        elif point == 0:
            pos_to = [pos[0], pos[1] - 1]
            if pos_to[1] < 0:
                pos_to[1] = 9
                wraparound = 2
            moving = True
        else:
            raise ValueError("direction must be in range(0, 4).")


def test_pressed() -> None:
    """
    If an arrow key is pressed, set moving to True; else set moving to False.
    """
    global moving
    k = pygame.key.get_pressed()
    moving = k[pygame.K_LEFT] or k[pygame.K_RIGHT] or k[pygame.K_UP] or k[pygame.K_DOWN]


def get_movement() -> None:
    k = pygame.key.get_pressed()
    if k[pygame.K_UP]:
        move(0)
    elif k[pygame.K_LEFT]:
        move(1)
    elif k[pygame.K_DOWN]:
        move(2)
    elif k[pygame.K_RIGHT]:
        move(3)


def mainloop() -> None:
    """
    Run the program.
    """
    init()
    global run
    run = True
    t = threading.Thread(target=drawcycle)
    t.daemon = True
    t.start()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_ESCAPE, pygame.K_BREAK, pygame.K_q]:
                    pygame.quit()
                    run = False
                    exit(0)
                elif not moving:
                    if event.key == pygame.K_UP:
                        move(0)
                    elif event.key == pygame.K_LEFT:
                        move(1)
                    elif event.key == pygame.K_DOWN:
                        move(2)
                    elif event.key == pygame.K_RIGHT:
                        move(3)


if __name__ == '__main__':
    mainloop()