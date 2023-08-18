s = input()


def solve(x, y, s):
    if len(s) == 0:
        return x, y

    if s[0] == "0":
        return solve(x, y, s[1:])
    elif s[0] == "1":
        return solve(x + pow(2, len(s) - 1), y, s[1:])
    elif s[0] == "2":
        return solve(x, y + pow(2, len(s) - 1), s[1:])
    else:
        return solve(x + pow(2, len(s) - 1), y + pow(2, len(s) - 1), s[1:])


print(len(s), *solve(0, 0, s))