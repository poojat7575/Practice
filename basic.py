def fibonacci(limit):
    output = []
    a, b = 0, 1
    while a <= limit:
        output.append(a)
        a,b = b, a+b
    return output

def fibonacci_optimized(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a,b = b, a+b

def factorial(number):
    if number < 0:
        return "Not Allowed"
    else:
        fact = 1
        for item in range(1, number+1):
            fact *= item
    return fact

def factorial_rec(number):
    if number < 0:
        return "Not Allowed"
    else:
        if number == 1:
            return number
        else:
            return number * factorial_rec(number-1)

def factors(n):
    output = []
    for i in range(1, (n//2)+1):
        if n % i == 0:
            output.append(i)
    return output

def armstrong(n):
    _n = n
    _sum = 0
    while n > 0:
        rem = n % 10
        _sum += rem ** 3
        n = n/10
    if _sum == _n:
        return True
    return False

def reverse_num(n):
    _n = 0
    while n > 0:
    _n = _n * 10 + (n % 10)
    n = n/10

if __name__ == "__main__":
    print(factors(100))
    print(factorial_rec(5))
    print(fibonacci(10))
    for i in fibonacci_optimized(10):
         print(i, end=', ')
