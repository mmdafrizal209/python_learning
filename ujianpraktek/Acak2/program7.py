def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

print("Faktorial dari 5:", faktorial(5))