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

    has_swapped = True

    while has_swapped == True:

        for i in range(len(cal_list) - 1):

            if (cal_list[i] > cal_list[i + 1]):

                has_swapped = True

                og = cal_list[i]
                new = cal_list[i + 1]

                cal_list[i] = new
                cal_list[i + 1] = og
            
            else:

                has_swapped = False

    print(f"Part 1 Solution: {max(cal_list)}")

    print(f"Part 2 Solution: {cal_list[0] + cal_list[1] + cal_list[2]}")
