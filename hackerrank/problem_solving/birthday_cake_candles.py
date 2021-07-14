"""
https://www.hackerrank.com/challenges/birthday-cake-candles/problem
"""
import collections


def birthday_cake_candles(candles: str) -> int:
    num_map = collections.defaultdict(int)
    for num in candles:
        num_map[num] += 1
    return max(num_map.values())

if __name__ == "__main__":
    _ = input()
    candles = input().split()
    print(birthday_cake_candles(candles))
    
