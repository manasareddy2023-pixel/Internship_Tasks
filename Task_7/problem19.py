# Problem: Weighted Uniform Strings
# Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input().strip()
n = int(input())

weights = set()
current_weight = 0
previous_char = ""

for char in s:
    weight = ord(char) - ord('a') + 1

    if char == previous_char:
        current_weight += weight
    else:
        current_weight = weight

    weights.add(current_weight)
    previous_char = char

for _ in range(n):
    x = int(input())

    if x in weights:
        print("Yes")
    else:
        print("No")