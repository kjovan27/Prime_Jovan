def is_prime(number):
    for num in range(number):
        if number % num == 0:
            return False

    return True

def print_next_prime(number):
    x = number
    while True:
        x += 1
        if is_prime(x):
            print(x)
