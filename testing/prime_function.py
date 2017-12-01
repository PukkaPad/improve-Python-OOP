

def is_prime(number):
    """Return True if number is prime."""
    if number <= 1:
        return False

    for num in range(2, number):
        if (number <= 1) | (number % num == 0):
            return False
    return True

def print_next_prime(number):
    "Print closest prime to number"
    i = number
    while True:
        i += 1
        if is_prime(i) == True:
            print(i)
            break


#print (is_prime(7))
#print_next_prime(7)

