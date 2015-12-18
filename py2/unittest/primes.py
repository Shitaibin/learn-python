def is_prime(n):
    """
    Judge n is an prime or not.
    If prime, return True, else False.
    """
    # n should be more than 1
    if n <= 1:
        return False
    # other cases
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_next_prime(n):
    """
    Get next prime after n.
    """
    x = n + 1
    while True:
        if (is_prime(x)):
            return x
        x += 1
    # not find prime
    return -1
