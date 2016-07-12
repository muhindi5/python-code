# working with recursion
def countdown(n):
    if(n == 0):
        print('go')
    else:
        print(n)
        countdown(n - 1)
inp = int(input('Enter limit:'))
countdown(inp)

# function to get the digital sum of a numbers
def sum_dig(n):
    if n == 1:
        return n;
    else:
        sum_dig(n - 1)
pr
