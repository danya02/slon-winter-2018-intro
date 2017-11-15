import sys

sys.setrecursionlimit(32768)

PATH, START, EXIT, VISITED, SOLUTION = tuple(" SE.!")


class Maze:
    def __init__(self, maze: [[str]], x: int, y: int, bound: bool = False):
        """
        A maze!

        maze is a list of lists of strings. Space is passable, and other characters are not.
        x and y are coordinates for start position (0-indexed).
        If bound, create a frame of exits around the maze. Useful when they are omitted.
        """
        maze_int = [list(i) for i in maze]
        if bound:
            self.maze = [[EXIT] * (len(maze[0]) + 2)]
            for i in maze_int:
                self.maze.append([EXIT] + i + [EXIT])
            self.maze.append([EXIT] * (len(maze[0]) + 2))
        else:
            self.maze = maze_int.copy()
        del maze_int
        self.start_y = y + int(bound)
        self.start_x = x + int(bound)
        self.solved = False

    def __repr__(self):
        return "\n".join("".join(row) for row in self.maze)

    def solve(self, x=None, y=None):
        """
        Solve the maze.
        This is recursive, so beware of using on large mazes.
        Raises ValueError if the start position is impassable.
        Raises EnvironmentError if the maze is unsolvable.
        """
        this_root = False
        if x is None:
            this_root = True
            x, y = self.start_x, self.start_y
        self.solved = True
        if self.maze[y][x] in (PATH, START):
            self.maze[y][x] = VISITED
            if self.solve(x + 1, y) or self.solve(x - 1, y) or self.solve(x, y + 1) or self.solve(x, y - 1):
                self.maze[y][x] = SOLUTION
                return True
        elif self.maze[y][x] == EXIT:
            return True
        elif self.maze[y][x] not in (PATH, START, EXIT, VISITED, SOLUTION) and this_root:
            self.solved = False
            raise ValueError('the start position is impassable')
        if this_root:
            self.solved = False
            raise EnvironmentError('maze is unsolvable')
        return False

    def get_sequence(self, output_maze: bool = False):
        """
        Get a sequence of characters in "<>^V" that describes a route out of the maze.
        If output_maze, map the sequence onto the original maze.
        """
        if not self.solved:
            raise EnvironmentError('maze not solved yet, use solve() first')
        x = self.start_x
        y = self.start_y
        output = ""
        repr_version = self.maze.copy()
        while True:
            if self.maze[y][x] is EXIT:
                return repr_version if output_maze else output
            elif self.maze[y][x] not in (PATH, START, EXIT, VISITED, SOLUTION):
                raise ValueError('walked into tile ({}, {}) that is impassable'.format(x, y))
            else:
                try:
                    if self.maze[y][x + 1] in (SOLUTION, EXIT):
                        output += ">"
                        repr_version[y][x] = ">"
                        y, x = y, x + 1
                    elif self.maze[y][x - 1] in (SOLUTION, EXIT):
                        output += "<"
                        repr_version[y][x] = "<"
                        y, x = y, x - 1
                    elif self.maze[y + 1][x] in (SOLUTION, EXIT):
                        output += "V"
                        repr_version[y][x] = "V"
                        y, x = y + 1, x
                    elif self.maze[y - 1][x] in (SOLUTION, EXIT):
                        output += "^"
                        repr_version[y][x] = "^"
                        y, x = y - 1, x
                except IndexError:
                    pass


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("The first argument should be a filename, or `-` for stdin.")
        exit(1)
    maze = ""
    if sys.argv[1] == '-':
        maze = sys.stdin.read()
    else:
        maze = open(sys.argv[1]).read()
    maze = [s for s in maze.split("\n") if s]

    x, y = maze[-1].split()
    maze = maze[:-1]
    x = int(x)
    y = int(y)
    mz = Maze(maze, x - 1, y - 1, True)
    try:
        mz.solve()
    except ValueError:
        raise RuntimeError("Cannot solve maze while suffocating.")
    except EnvironmentError:
        raise RuntimeError("Maze appears to have no exit.")
    print(mz.get_sequence())
