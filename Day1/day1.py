with open("cal_data.txt") as cal:


    cal_list = []

    elf_sum = 0

    for l in cal:

        l.strip()

        if l is not "\n":

            elf_sum += int(l)

        else:

            cal_list.append(elf_sum)

            elf_sum = 0

    sorted_list = cal_list.sort(reverse=True)

    print(f"Part 1 Solution: {max(sorted_list)}")

    print(f"Part 2 Solution: {sorted_list[0] + sorted_list[1] + sorted_list[2]}")
