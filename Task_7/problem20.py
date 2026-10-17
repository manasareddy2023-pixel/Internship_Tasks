# Problem: Super Reduced String
# Link: https://www.hackerrank.com/challenges/reduced-string/problem

s = input().strip()
stack = []

for char in s:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)

result = "".join(stack)

if result:
    print(result)
else:
    print("Empty String")