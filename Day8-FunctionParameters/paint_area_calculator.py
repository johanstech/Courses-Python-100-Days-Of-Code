import math


def paint_area_calc(height, width, coverage):
    return math.ceil((height * width) / coverage)


wall_height = int(input("Enter wall height: "))
wall_width = int(input("Enter wall width: "))

can_coverage = 5

paint_cans_needed = paint_area_calc(
    height=wall_height, width=wall_width, coverage=can_coverage)

print(f"You need to buy {paint_cans_needed} cans of paint for this wall.")
