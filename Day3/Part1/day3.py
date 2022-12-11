from string import ascii_lowercase, ascii_uppercase


with open("i.txt", "r") as f:

    data = f.read()


sums = 0

for line in data.split("\n"):

    p1 = line[:len(line)//2]
    p2 = line[len(line)//2:]

    r = set(p1).intersection(p2)

    for i in r:

        if i in ascii_lowercase:

            sums += ascii_lowercase.index(i) + 1

        elif i in ascii_uppercase:
            
            sums += ascii_uppercase.index(i) + 27

print("Part 1:", sums)
