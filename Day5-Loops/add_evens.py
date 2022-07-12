sum_even_numbers = 0

# for num in range(2, 100, 2):
#     sum_even_numbers += num

for num in range(101):
    if num % 2 == 0:
        sum_even_numbers += num

print("Sum of even numbers from 0 to 100 is:", sum_even_numbers)
