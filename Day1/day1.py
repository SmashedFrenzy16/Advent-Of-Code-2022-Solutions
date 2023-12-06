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

    cal_list.sort(reverse=True)

    cal_list_3_sum = cal_list[0] + cal_list[1] + cal_list[2]

    print(f"Part 1 Solution: {max(cal_list)}")

    print(f"Part 2: {cal_list_3_sum}")
