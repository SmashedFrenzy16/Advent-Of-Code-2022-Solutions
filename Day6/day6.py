from sys import *

def file_range(file):

    return range(len(file))

def parse(file, line, digit):

    return len(set(file[line: line + digit]))

with open("p_input.txt") as f:

    file = f.read().strip()

    for line in file_range(file):

        if parse(file, line, 4) is 4:

            print(f"Part 1 Solution: {line + 4}")

            break

    for line in file_range(file):

        if parse(file, line, 14) is 14:

            print(f"Part 2 Solution: {line + 14}")

            break
exit()
