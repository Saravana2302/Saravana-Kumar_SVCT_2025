Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> """
Function Description

Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name
Prints

string: 'Hello  ! You just delved into python' where  and  are replaced with  and .
Input Format

The first line contains the first name, and the second line contains the last name.

Constraints

The length of the first and last names are each ≤ .

Sample Input 0

Ross
Taylor
Sample Output 0

Hello Ross Taylor! You just delved into python.
Explanation 0

The input read by the program is stored as a string data type. A string is a collection of characters.

"""
"\nFunction Description\n\nComplete the print_full_name function in the editor below.\n\nprint_full_name has the following parameters:\n\nstring first: the first name\nstring last: the last name\nPrints\n\nstring: 'Hello  ! You just delved into python' where  and  are replaced with  and .\nInput Format\n\nThe first line contains the first name, and the second line contains the last name.\n\nConstraints\n\nThe length of the first and last names are each ≤ .\n\nSample Input 0\n\nRoss\nTaylor\nSample Output 0\n\nHello Ross Taylor! You just delved into python.\nExplanation 0\n\nThe input read by the program is stored as a string data type. A string is a collection of characters.\n\n"

>>> def print_full_name(first, last):
    full_name = f'Hello {first} {last}! You just delved into python.'
    print(full_name)
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)