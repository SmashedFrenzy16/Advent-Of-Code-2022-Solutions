points = 0

with open("input.txt") as f:


    l = f.read().split("\n")

    for i in l:

        temp_arr = [_ for _ in i.split(" ")]


        if temp_arr[1] == "X":

            points += 1

            if temp_arr[0] == "A":

                points += 3

            if temp_arr[0] == "C":

                points += 6

        if temp_arr[1] == "Y":

            points += 2

            if temp_arr[0] == "A":

                points += 6

            if temp_arr[0] == "B":

                points += 3
        
        if temp_arr[1] == "Z":

            points += 3

            if temp_arr[0] == "B":

                points += 6

            if temp_arr[0] == "C":

                points += 3

print(points)
