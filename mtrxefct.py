import random
import time

# Define the characters to be used in the matrix effect
matrix_chars = ['0', '1']

# Define the size of the matrix screen
rows, columns = 40, 120

# Define the speed of the matrix effect
delay = 0.1

# Define a function to print a random matrix character in a given color
def print_char():
    char = random.choice(matrix_chars)
    color_code = random.randint(30, 37)
    print(f"\033[{color_code}m{char}\033[0m", end='')

# Define the main function that creates the matrix effect
def matrix_effect():
    while True:
        # Create a new row of matrix characters
        row = [random.choice(matrix_chars) for _ in range(columns)]

        # Print the row of matrix characters with a slight delay
        for char in row:
            print_char()
            time.sleep(delay)

        # Move the cursor back to the beginning of the row
        print("\033[1A", end='')

# Call the main function to start the matrix effect
matrix_effect()


Here's how the program works:

We start by defining the characters to be used in the matrix effect (matrix_chars), as well as the size of the matrix screen (rows and columns) and the speed of the effect (delay).
We then define a function print_char() that prints a random matrix character in a random color.
The main function matrix_effect() creates an infinite loop that generates a new row of matrix characters, prints them one at a time with a slight delay, and then moves the cursor back to the beginning of the row to start over.
Finally, we call the matrix_effect() function to start the matrix effect.
To run the program, simply save it to a file (e.g. matrix.py) and then run it from the command line using the python command:

python matrix.py
