import fileinput
from collections import defaultdict

dirs = defaultdict(list)
current_location = ''
dir_totals = []


def process_line3(line: str):
    global current_location, dirs
    line = line.strip()
    line_items = line.split(" ")

    if line.startswith("$ ls"):
        pass

    if line.startswith("dir"):
        if line_items[1] == "/":
            dirs[current_location].append(current_location + line_items[1])
        else:
            dirs[current_location].append(current_location + line_items[1] + '/')
        return

    if line.startswith("$ cd"):
        if line.endswith(".."):
            current_location = current_location[:current_location[:-1].rindex('/')+1]
            return
        if line_items[2] == "/":
            current_location = current_location + line_items[2]
        else:
            current_location = current_location + line_items[2] + '/'
        return

    try:
        dirs[current_location].append(int(line_items[0]))
    except ValueError:
        pass


for line in fileinput.input():
    if line:
        process_line3(line)


def sum_dir(a: list) -> int:
    dir_sum = 0
    for v in a:
        try:
            dir_sum += int(v)
        except ValueError:
            dir_sum += sum_dir(dirs[v])
    dir_totals.append(dir_sum)
    return dir_sum


print(f"Part 1: ")
sum_dirs = sum_dir(dirs["/"])
print(sum([t for t in dir_totals if t <= 100000]))

print(f"Part 2: ")
total = dir_totals[-1]
total_disk_space = 70000000
total_free_space = 30000000

unused_space = total_disk_space - total
space_needed = total_free_space - unused_space

could_delete_dirs = [d for d in dir_totals if d >= space_needed]

print(min(could_delete_dirs))
