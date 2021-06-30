"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""

name_scores = dict()
for _ in range(int(input())):
    name, *scores = input().split()
    name_scores[name] = scores
scores = name_scores[input()]
print("{:.2f}".format(sum([float(score) for score in scores])/len(scores)))