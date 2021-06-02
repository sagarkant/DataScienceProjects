'''
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring
occurs in the given string. String traversal will take place
from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format
The first line of input contains the original string.
The next line contains the substring.
'''

string=input()
substring=input()
count=0
for i in range(len(string)-len(substring)+1): # range excludes the upper bound
    if string[i:i+len(substring)]==substring:
        count+=1
print(count)

