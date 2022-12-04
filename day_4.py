import fileinput
import re

fully_contain = 0
any_overlap = 0


def process_line(line: str):
    global fully_contain, any_overlap
    ranges = re.split(',|-', line.strip())

    range_1 = range(int(ranges[0]), int(ranges[1])+1)
    range_2 = range(int(ranges[2]), int(ranges[3])+1)

    overlap = list(set(range_1) & set(range_2))
    if len(overlap) == len(range_1) or len(overlap) == len(range_2):
        fully_contain += 1
    if len(overlap) > 0:
        any_overlap += 1


for line in fileinput.input():
    if line:
        process_line(line)


print(f"Part 1: {fully_contain}")
print(f"Part 2: {any_overlap}")
