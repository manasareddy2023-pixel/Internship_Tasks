# Problem: Making Anagrams
# Link: https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

s1 = Counter(input().strip())
s2 = Counter(input().strip())

deletions = sum((s1 - s2).values()) + sum((s2 - s1).values())

print(deletions)