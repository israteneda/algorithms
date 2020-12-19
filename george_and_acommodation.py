"""
George has recently entered the BSUCP (Berland State University for Cool Programmers). George has a friend Alex who has also entered the university. Now they are moving into a dormitory.

George and Alex want to live in the same room. The dormitory has n rooms in total. At the moment the i-th room has pi people living in it and the room can accommodate qi people in total (pi ≤ qi). Your task is to count how many rooms has free place for both George and Alex.

Input
The first line contains a single integer n (1 ≤ n ≤ 100) — the number of rooms.

The i-th of the next n lines contains two integers pi and qi (0 ≤ pi ≤ qi ≤ 100) — the number of people who already live in the i-th room and the room's capacity.

Output
Print a single integer — the number of rooms where George and Alex can move in.
"""

import io
from unittest import mock
from unittest.mock import patch

def solve():
    rooms = int(input())
    available_rooms = 0
    for _ in range(rooms):
        p, q = input().split(' ')
        if p < q:
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

    assert  mock_stdout.getvalue() == '0\n2\n'
    
