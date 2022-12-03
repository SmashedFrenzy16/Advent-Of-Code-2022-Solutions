data = open("input.txt").read()

score = 0

for i in data.split("\n"):

    c, h = i.split()

    if h == "X":

        if c == "A":

            score += 3

        if c == "B":

            score += 1

        if c == "C":

            score += 2

        score += 0

    if h == "Y":

        if c == "A":

            score += 1

        if c == "B":

            score += 2

        if c == "C":

            score += 3

        score += 3

    if h == "Z":

        if c == "A":

            score += 2

        if c == "B":

            score += 3

        if c == "C":

            score += 1

        score += 6

print("Maxium score achievable for part 2:", score)