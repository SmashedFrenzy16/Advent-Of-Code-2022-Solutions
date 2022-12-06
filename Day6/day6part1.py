import sys



with open("i.txt", "r") as inp:

    data = inp.read()


for i in range(len(data)):

    if len(set(data[i:i+4])) == 4:

        print("Letters are (Part 1):", i + 4)

        sys.exit()