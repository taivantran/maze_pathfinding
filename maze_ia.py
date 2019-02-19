#!/usr/bin/env python3
import sys
import random
import collections
import string

# Get a list of 26 alphabet
alp = list(string.ascii_uppercase)

def getBoard():
   board = []
   while True:
       x = sys.stdin.readline()
       if x[0] != "#":
           break
       board.append(x.rstrip('\n'))
   return board


def find_location(l, letter):
    for y in range(len(l)):
        for x in range(len(l[y])):
            if l[y][x] == letter:
                return [y,x]


# Breath_finding path
def bfs(grid, start):
    small = []
    queue = collections.deque([[start]])
    seen = list(start)
    while queue:
        path = queue.popleft()
        y, x = path[-1]
        if grid[y][x] == '!' and len(path) < 20:
            return path
        elif grid[y][x] == 'o':
            small.append(path)
        for x2, y2 in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if grid[y2][x2] != '#' and [y2, x2] not in seen and grid[y2][x2] not in alp:
                queue.append(path + [[y2, x2]])
                seen.append([y2, x2])
    if len(small) > 0:
        path = min(small, key=len)
        return path


def move(ls, letter, maze):
    # IF list move (ls) is NONE
    if not ls:
        char = find_location(maze,letter)
        if maze[char[0] + 1][char[1]] != '#' and maze[char[0] + 1][char[1]] not in alp:
            return "MOVE DOWN\n\n"
        elif maze[char[0] - 1][char[1]] != '#' and maze[char[0] - 1][char[1]] not in alp:
            return "MOVE UP\n\n"
        elif maze[char[0]][char[1] - 1] != '#' and maze[char[0]][char[1] - 1] not in alp:
            return "MOVE LEFT\n\n"
        elif maze[char[0]][char[1] + 1] != '#' and maze[char[0]][char[1] + 1] not in alp:
            return "MOVE RIGHT\n\n"
    # IF ls is a list of valid moves
    if ls[1][0] - ls[0][0] == 1:
        return "MOVE DOWN\n\n"
    elif ls[1][0] - ls[0][0] == -1:
        return "MOVE UP\n\n"
    elif ls[1][1] - ls[0][1] == -1:
        return "MOVE LEFT\n\n"
    elif ls[1][1] - ls[0][1] == 1:
        return "MOVE RIGHT\n\n"


def main():
    s = sys.stdin.readline()
    while s != '':
        if "HELLO" in s:
            sys.stdout.write("I AM TAI\n\n")
        elif "YOU ARE" in s:
            letter = s[-2]
            sys.stdout.write("OK\n\n")
        elif "MAZE" in s:
            l = getBoard()

            lst = bfs(l, find_location(l, letter))
            sys.stdout.write(move(lst, letter, l))
            # sys.stdout.write("MOVE UP\n\n")
        s = sys.stdin.readline()


if __name__ == "__main__":
    main()
