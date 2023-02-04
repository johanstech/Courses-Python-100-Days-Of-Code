def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    return is_prime


n = int(input("Enter number to check if prime: "))
is_prime = prime_checker(number=n)

if is_prime:
    print("It's a prime number!")
else:
    print("It's not a prime number.")
