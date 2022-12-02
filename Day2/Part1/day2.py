data = open("input.txt").read()

score = 0

for i in data.split("\n"):

    c, h = i.split()

    if h == "X":

        if c == "A":

            score += 3

        if c == "C":

            score += 6

        score += 1

    if h == "Y":

        if c == "A":

            score += 6

        if c == "B":

            score += 3

        score += 2

    if h == "Z":

        if c == "B":

            score += 6

        if c == "C":

            score += 3

        score += 3

print("Maximum score with strategy:", score)