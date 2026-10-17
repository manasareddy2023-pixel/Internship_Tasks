# Problem: The Minion Game
# Link: https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    length = len(string)
    for i in range(length):
        if string[i] in "AEIOU":
            kevin += length - i
        else:
            stuart += length - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)