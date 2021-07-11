"""
https://www.hackerrank.com/challenges/python-lists/problem
"""

def solve():
    N = int(input())
    list_ = list()
    for _ in range(N):
        action, *numbers = input().split()
        nums = list(map(int, numbers))
        if action == "insert":
            position, element = nums
            list_.insert(position, element)
        elif action == "print":
            print(list_)
        elif action == "remove" or action == "append":
            eval(f"list_.{action}({nums[0]})")
        else:
            eval(f"list_.{action}()")


if __name__ == '__main__':
    solve()
