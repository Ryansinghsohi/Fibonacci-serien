# Funktion för att generera Fibonacci-serien upp till ett visst tal 'n'
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    while a <= n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

# Anropa funktionen för att generera Fibonacci-serien upp till length
fib_length = int(input("how long do you want the series to be:"))
fibonacci_numbers = generate_fibonacci(fib_length)

# Skriv ut Fibonacci-serien
print("Fibonacci-serien upp till 50:")
for num in fibonacci_numbers:
    print(num, end=" ")
