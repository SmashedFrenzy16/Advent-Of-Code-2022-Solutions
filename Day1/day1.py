
cal_list = []

elf_sum = 0

def elf_sort(cal_file: str) -> list:

    global elf_sum

    with open(cal_file) as c:

        for i in c:

            if i != "\n":

                elf_sum += int(i)

            else:

                cal_list.append(elf_sum)

                elf_sum = 0

max_elf = elf_sort("cal_data.txt")

cal_list.sort(reverse=True)

print("Most calories elf: ", max(cal_list))

cal_list_3_sum = cal_list[0] + cal_list[1] + cal_list[2]

print("Combined calories of top 3 elves: ", cal_list_3_sum)