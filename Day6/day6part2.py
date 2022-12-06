import sys



with open("i.txt", "r") as inp:

    data = inp.read()


for i in range(len(data)):

    if len(set(data[i:i+14])) == 14:

        print("Letters are (Part 2):", i + 14)

        sys.exit()