# Problem: Pangrams
# Link: https://www.hackerrank.com/challenges/pangrams/problem

s = input().lower()

if set(s) >= set("abcdefghijklmnopqrstuvwxyz"):
    print("pangram")
else:
    print("not pangram")