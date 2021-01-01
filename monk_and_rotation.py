"""
Monk and Rotation
https://www.hackerearth.com/practice/codemonk/
"""

from collections import deque


def solve(K, A):
    for _ in range(K):
        last_item = A.pop()
        A.appendleft(last_item)
    return " ".join(A)


def main():
    for _ in range(int(input())):
        _, K = [int(num) for num in input().split()]
        A = deque(input().split())
        print(solve(K, A))


if __name__ == "__main__":
    main()


def test():
    assert solve(2, deque(["1", "2", "3", "4", "5"])) == "4 5 1 2 3"
