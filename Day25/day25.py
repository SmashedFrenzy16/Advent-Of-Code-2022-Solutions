with open("i.txt") as file:

    lines = file.read().split()

s_d = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2
}

d_s = {

    3: "=",
    4: "-",
    5: "0",
    6: "1",
    7: "2"
}


def snafu_int(s):

    return sum((pow(5, i) * s_d[c] for i, c in enumerate(s[::-1])))


def int_snafu(d):

    s = []

    while d:

        s.append(d % 5)
        d //= 5

    for i in range(len(s)):

        if s[i] >= 3:

            s[i] = d_s[s[i]]
            s[i+1] += 1

        if isinstance(s[i], int):

            s[i] = str(s[i])

    return "".join(reversed(s))


solution = int_snafu(sum(snafu_int(line) for line in lines))

print("Solution:", solution)
print("Merry Christmas to those celebrating and a Happy New Year!")
