#!/usr/bin/python3
import sys

def main():
    #command line args are contained in the in sys.argv list
    #sys.argv[0] is the name of the file while [1] is the first argument
    print('Hello', sys.argv[1])

#standard boilerplate to call the main() function to begin program
#special variable __name__ will be set to __main__ if this python file is run directly, when imported by another module the code is not run
if __name__ == '__main__':
    main()

