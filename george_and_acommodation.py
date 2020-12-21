"""
A. George and Accommodation
https://codeforces.com/problemset/problem/467/A
"""

import io
from unittest import mock
from unittest.mock import patch


def solve():
    rooms = int(input())
    available_rooms = 0
    for _ in range(rooms):
        p, q = [int(num) for num in input().split(' ')]
        if p + 2 <= q:
            available_rooms += 1
    print(available_rooms)


@patch('sys.stdout', new_callable=io.StringIO)
def test(mock_stdout):
    user_input = [
        '3',
        '1 1',
        '2 2',
        '3 3',
        '3',
        '1 10',
        '0 10',
        '10 10',
    ]

    with patch('builtins.input', side_effect=user_input):
        for _ in range(2):
            solve()

    assert mock_stdout.getvalue() == '0\n2\n'


if __name__ == '__main__':
    solve()
