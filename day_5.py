import fileinput
from collections import defaultdict
import re
from textwrap import wrap

stacks = defaultdict(list)


def process_stack_line(line: str):
    global stacks
    # wrap ignores whitespace, so swap with a random character
    line = line.strip().replace(" ", "?")
    boxes = [a[:3] for a in wrap(line, 4)]

    for i, box in enumerate(boxes):
        if box == "???":
            continue
        stacks[i+1].append(box)


def process_line(line: str):
    global stacks
    digits = re.findall(r'\d+', line)
    num_moves = digits[0]
    for move in range(int(num_moves)):
        to_move = stacks.get(int(digits[1])).pop(0)
        existing_line = stacks.get(int(digits[2]))
        stacks[int(digits[2])] = [to_move, *existing_line]


def process_line_pt_2(line: str):
    global stacks
    digits = re.findall(r'\d+', line)
    num_moves = digits[0]
    to_move = []
    for move in range(int(num_moves)):
        to_move.append(stacks.get(int(digits[1])).pop(0))
    existing_line = stacks.get(int(digits[2]))
    stacks[int(digits[2])] = [*to_move, *existing_line]


for line in fileinput.input():
    if line[0] == "[":
        process_stack_line(line)
    elif line[0] == "m":
        # process_line(line)
        process_line_pt_2(line)


top_of_stacks = [value[0] for key, value in sorted(stacks.items())]
print(top_of_stacks)
