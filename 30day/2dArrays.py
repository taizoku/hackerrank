'''
Changelog 01/02/18
 - Added some stuff for Jameseses peace of mind
    - Some shitty functions
    - Print methods and crap
'''

# !/bin/python3


# Just prints the input array to stdout
def print_array():
    printer = 0
    while printer < 6:
        print(arr[printer])
        printer += 1

'''
def calculate_hourglass_sum():
    hourglass_num = 0
    y = down
    # print("Down count is:", down)
    x = across
    # print("Across count is:", across)

    row_counter = col_counter = 0
    calc_sum = 0

    while hourglass_num < 7:
        calc_sum += arr[x][y]

        print("rowCounter is now:", row_counter)
        print("colCounter is now:", col_counter)
        print("Sum is", "arr[", y, "][", x, "] =", calc_sum)

        if (row_counter == 0 and col_counter == 2) or (row_counter == 1):
            y += 1
            x -= 1
            row_counter += 1
            col_counter -= 1

        else:
            x += 1
            col_counter += 1

        hourglass_num += 1

        return calc_sum
'''

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

# print_array()

down = 0
calculationSum = maxSum = -1000

while down < 4:
    across = 0

    while across < 4:

        hourglass_num = 0
        y = down
        # print("Down count is:", down)
        x = across
        # print("Across count is:", across)

        row_counter = col_counter = 0
        calculationSum = 0

        while hourglass_num < 7:
            calculationSum += arr[y][x]

            print("rowCounter is now:", row_counter)
            print("colCounter is now:", col_counter)
            print("Sum is", "arr[", y, "][", x, "] =", calculationSum)

            if (row_counter == 0 and col_counter == 2) or (row_counter == 1):
                y += 1
                x -= 1
                row_counter += 1
                col_counter -= 1

            else:
                x += 1
                col_counter += 1

            hourglass_num += 1

        across += 1
        maxSum = max(maxSum, calculationSum)
    down += 1
print(maxSum)
