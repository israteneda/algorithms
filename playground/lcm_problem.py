"""
A. LCM Problem
https://codeforces.com/problemset/problem/1389/A
"""

def solve(numbers):
    l, r = map(int, numbers.split())
    if 2 * l <= r:
        return f"{l} {2 * l}"
    else:
        return "-1 -1"

def main():
    cases = int(input())
    for _ in range(cases):
        print(solve(input()))

if __name__ == "__main__":
    main()

def test():
   assert solve("1 1337") == "1 2"
   assert solve("13 69") == "13 26"
   assert solve("2 4") == "2 4"
   assert solve("88 89") == "-1 -1"

