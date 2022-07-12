heights = [180, 132, 156, 174, 193, 149, 166, 170, 182]

num_heights = 0
sum_heights = 0
for height in heights:
    sum_heights += height
    num_heights += 1

average_height = round(sum_heights / num_heights)
print("Average height:", average_height)
