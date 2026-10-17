# Problem: Funny String
# Link: https://www.hackerrank.com/challenges/funny-string/problem
#!/bin/python3

import os

def funnyString(s):
    r = s[::-1]

    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return "Not Funny"

    return "Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for _ in range(t):
        s = input().strip()
        result = funnyString(s)
        fptr.write(result + '\n')

    fptr.close()