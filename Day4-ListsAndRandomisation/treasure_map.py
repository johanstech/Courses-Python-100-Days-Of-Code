row1 = ["⬜", "⬜", "⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜", "⬜", "⬜"]
row4 = ["⬜", "⬜", "⬜", "⬜", "⬜"]
row5 = ["⬜", "⬜", "⬜", "⬜", "⬜"]

treasure_map = [row1, row2, row3, row4, row5]

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")

position_input = input(
    "Where do you want to put the treasure? Row and column, separated by comma.\n")

position = position_input.split(", ")
row_pos = int(position[0]) - 1
column_pos = int(position[1]) - 1

treasure_map[row_pos][column_pos] = "❌"

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
