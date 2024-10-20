"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n 'H'characters in the file.
"""


def minOperations(n):
    """
    takes the number n of 'H' characters I want to show in the file
    and returns the number of operations

    input:
        n: number of 'H' characters
    Return:
        operations: fewest number of operations to do
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Keep dividing the number n by its smallest prime factors
    while n > 1:
        while n % divisor == 0:
            # Each factor contributes its value to the number of operations
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
