with open("i.txt") as inp:

    data = inp.read().split("\n")


cycles = 0

x = 1


cycle_intervals = set([20, 60, 100, 140, 180, 220])

signal = 0

for line in data:

    if "addx" in line:

        time = 2

        while time > 0:



            cycles += 1

            if cycles in cycle_intervals:

                signal += (cycles * x)

            time -= 1

        x += int(line[5:])


    if "noop" in line:

        cycles += 1

        if cycles in cycle_intervals:

            signal += (cycles * x)

print(signal)






