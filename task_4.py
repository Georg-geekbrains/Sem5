"""
Создайте функцию генератор чисел Фибоначчи
"""

def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_sequence()
for _ in range(13):
    print(next(fib))