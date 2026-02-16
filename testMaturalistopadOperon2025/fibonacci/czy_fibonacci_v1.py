def czy_fibonacci(k):
    if k < 0:
        return False
    a, b = 0, 1
    while a < k:
        a, b = b, a + b
    return a == k