"""
A. Vanya and Fence
https://codeforces.com/problemset/problem/677/A
"""


def solve(friends, height):
    width = 0

    for friend in friends:
        width += 2 if friend > height else 1

    return width


if __name__ == "__main__":
    _, height = [int(x) for x in input().split()]
    friends = [int(friend) for friend in input().split()]

    print(solve(friends, height))


def test():
    assert solve([4, 5, 14], 7) == 4
    assert solve([1, 1, 1, 1, 1, 1], 6) == 6
    assert solve([7, 6, 8, 9, 10, 5], 5) == 11
