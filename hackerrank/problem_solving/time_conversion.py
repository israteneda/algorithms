"""
https://www.hackerrank.com/challenges/time-conversion/problem
"""


def convert_time(input_time: str) -> str:
    time_, am_pm = input_time[:-2], input_time[-2:]
    h = int(time_[:2])
    if am_pm == "PM" and h != 12:
        h += 12
    if am_pm == "AM" and h == 12:
        h = 0
    return f"{h:02d}" + time_[2:]


if __name__ == "__main__":
    input_time = input()
    print(convert_time(input_time))