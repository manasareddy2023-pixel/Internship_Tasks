# Problem: CamelCase
# Link: https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()

if not s:
    print(0)
else:
    words = 1

    for char in s:
        if char.isupper():
            words += 1

    print(words)