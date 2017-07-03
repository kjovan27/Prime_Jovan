def is_prime(number):
    if number <= 0:
        return False
    if number in (0, 1):
        return False
    for num in range(2, number):
        if number % num == 0:
            return False

    return True

def print_next_prime(number):
    x = number
    while True:
        x += 1
        if is_prime(x):
            print(x)
