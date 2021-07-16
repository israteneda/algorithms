"""
https://www.hackerrank.com/challenges/apple-and-orange/problem
"""


def filter_fruit(house_start, house_end, three_position):
    return lambda fruit: (
        three_position + fruit >= house_start and three_position + fruit <= house_end
    )


def get_length(filtered_fruits):
    return len(list(filtered_fruits))


def count_apples_and_oranges(s, t, a, b, apples, oranges):
    print(get_length(filter(filter_fruit(s, t, a), apples)))
    print(get_length(filter(filter_fruit(s, t, b), oranges)))


def process_input():
    return list(map(int, input().split()))


if __name__ == '__main__':
    s, t = process_input()
    a, b = process_input()
    _, _ = process_input()  # apples and oranges lengths
    apples = process_input()
    oranges = process_input()
    count_apples_and_oranges(s, t, a, b, apples, oranges)