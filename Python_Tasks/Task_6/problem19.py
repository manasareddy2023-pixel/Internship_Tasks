# Problem: Company Logo
# Link: https://www.hackerrank.com/challenges/most-commons/problems
if __name__ == '__main__':
    from collections import Counter
    s = input()
    counts = Counter(s)

for character, count in sorted(
    counts.items(),
    key=lambda item: (-item[1], item[0])
)[:3]:
    print(character, count)