from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '/',
           '{', '(', '[', ')', ']', '=', '}', '+', '?', '.', ':', ',', ';', '-', '_']

print("Welcome to the Python Password Generator.")
nr_letters = int(input("How many letters for you like in your password?\n"))
nr_numbers = int(input("How many numbers for you like in your password?\n"))
nr_symbols = int(input("How many symbols for you like in your password?\n"))

pw_length = nr_letters + nr_numbers + nr_symbols

pw_list = []
for letter in range(nr_letters):
    pw_list.append(choice(letters))

for number in range(nr_numbers):
    pw_list.append(choice(numbers))

for symbor in range(nr_symbols):
    pw_list.append(choice(symbols))

for i in range(10):
    shuffle(pw_list)

password = ""
for char in pw_list:
    password += char

print(password)
