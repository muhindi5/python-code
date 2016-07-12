# Example of recursive function to find the factorial of a number 
def rec_fac(x):
    if(x) == 1:
        return 1;
    else:
        return (x * rec_fac(x-1))

num = int(input('Enter the Number:'))
if num >=0:
        print('The factorial of the number is: ',rec_fac(num))

