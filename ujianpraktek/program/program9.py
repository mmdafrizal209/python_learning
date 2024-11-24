def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

n = int(input("Masukkan jumlah bilangan Fibonacci yang ingin dicetak: "))

hasil = fibonacci(n)

print(f"Deret Fibonacci sebanyak {n} bilangan: {hasil}")