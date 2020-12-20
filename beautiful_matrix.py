""" 
A. Beautiful Matrix
https://codeforces.com/problemset/problem/263/A
"""

import io
from unittest import mock
from unittest.mock import patch

def solve():
    matrix = []
    moves = 0

    for _ in range(5):
        row = input().split()
        matrix.append(row)

    while matrix[2][2] != '1':
        for r, row in enumerate(matrix): 
            if '1' in row:
                
                for c, column in enumerate(row):
                    if column == '1':
                        if c < 2:
                            matrix[r][c], matrix[r][c + 1] = matrix[r][c + 1], matrix[r][c]
                            moves += 1
                        elif c > 2:
                            matrix[r][c], matrix[r][c - 1] = matrix[r][c - 1], matrix[r][c]
                            moves += 1

                if r < 2:
                    matrix[r], matrix[r + 1] = matrix[r + 1], matrix[r]
                    moves += 1
                elif r > 2:
                    matrix[r], matrix[r - 1] = matrix[r - 1], matrix[r]
                    moves += 1

    print(moves) 

if __name__ == '__main__':
    solve()

@patch('sys.stdout', new_callable=io.StringIO)
def test(mock_stdout):
    user_input = [
            '0 0 0 0 0',
            '0 0 0 0 1',
            '0 0 0 0 0',
            '0 0 0 0 0',
            '0 0 0 0 0',
            '0 0 0 0 0',
            '0 0 0 0 0',
            '0 1 0 0 0',
            '0 0 0 0 0',
            '0 0 0 0 0',
            ]

    with patch('builtins.input', side_effect=user_input):
        for _ in range(2):
            solve()

    assert mock_stdout.getvalue() == '3\n1\n'


