# Problem: Piling Up!
# Link: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))

    current = float("inf")
    possible = True

    while blocks:
        if blocks[0] >= blocks[-1]:
            chosen = blocks.popleft()
        else:
            chosen = blocks.pop()

        if chosen > current:
            possible = False
            break

        current = chosen

    print("Yes" if possible else "No")