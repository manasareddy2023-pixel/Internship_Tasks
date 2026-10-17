# Problem: Game of Thrones - I
# Link: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

s = input().strip()
freq = Counter(s)

odd_counts = sum(1 for count in freq.values() if count % 2 != 0)

if odd_counts <= 1:
    print("YES")
else:
    print("NO")