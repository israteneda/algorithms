"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""

s = dict()
for _ in range(int(input())):
    n, sc = input().split(" ", 1)
    s[n] = sc
ss = s[input()].split(" ")
print("{:.2f}".format(sum([float(i) for i in ss])/len(ss)))