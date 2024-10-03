'''

2)Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
program:

def is_factorial(num):
    # Initialize variables
    factorial = 1
    i = 1
    
    # Calculate factorial iteratively
    while factorial < num:
        i += 1
        factorial *= i
    
    # Check if the calculated factorial is equal to the number
    return factorial == num

# Input: Read an integer n
n = int(input())

# Output: Determine if n is a factorial number
if is_factorial(n):
    print("Yes")
else:
    print("No")
'''
