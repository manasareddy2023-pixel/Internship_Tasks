# Problem: Write a Function
# Link: https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
# Write your logic here
    leap = False
    if   year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

year = int(input())