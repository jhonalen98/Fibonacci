def fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Imprimir los primeros 50 números de la sucesión de Fibonacci
n = 50
fib_sequence = fibonacci_sequence(n)
for index, value in enumerate(fib_sequence):
    print(f"{index + 1}: {value}")