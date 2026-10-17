# Problem: Anagram
# Link: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    if n % 2 != 0:
        print(-1)
    else:
        first = Counter(s[:n // 2])
        second = Counter(s[n // 2:])

        print(sum((first - second).values()))