"""
https://www.hackerrank.com/challenges/plus-minus/problem
"""


def plus_minus(arr):
    p = list()
    n = list()
    for num in arr:
        if num > 0:
            p.append(num)
        if num < 0:
            n.append(num)
    t = len(arr)
    lp = len(p)
    ln = len(n)
    print(
        "{:.6f}\n{:.6f}\n{:.6f}".format(
            lp/t,
            ln/t,
            (t - (lp + ln))/t,
        )
    )


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().split()))

    plus_minus(arr)
