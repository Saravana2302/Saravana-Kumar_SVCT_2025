# Task
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20 , print Weird
# If n is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird

i=int(input())
if (i%2 ==1) or (i%2==0 and 6<=i<=20):
    print("Weird")
elif (i%2==0 and 2<=i<=5) or (i%2==0 and i>20):
    print("Not Weird")
