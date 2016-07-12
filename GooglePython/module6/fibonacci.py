# generate fibonacci numbers using recursion
def get_fib(n):
    if n == 1:
        return n
    else:
        return (n - 2) + get_fib(n - 1)
        #return get_fib(n - 2) + get_fib(n - 1)

number = int(input('Enter the Number:'))
print('Fibonacci Result of %d is %d' % (number,get_fib(number)))
