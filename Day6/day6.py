from sys import *

def parse(file, line, digit):

    return len(set(file[line: line + digit]))

with open("p_input.txt") as f:

    file = f.read().strip()

    for line in range(len(file)):

        if parse(file, line, 4) == 4:

            print(f"Part 1 Solution: {line + 4}")

            break

    for line in range(len(file)):

        if parse(file, line, 14) == 14:

            print(f"Part 2 Solution: {line + 14}")

            break
exit()
