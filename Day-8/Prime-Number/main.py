number = int(input("Enter a number: "))


def prime_checker(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False

    if is_prime:
        print(f"number {n} is prime number")
    else:
        print(f"number {n} is not prime number")


prime_checker(number)
