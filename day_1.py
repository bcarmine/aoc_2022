import fileinput

elf_totals = []
current_elf_total = 0


def process_line(line: str):
    global current_elf_total, elf_totals

    try:
        current_elf_total += int(line)
    except ValueError:
        elf_totals.append(current_elf_total)
        current_elf_total = 0


for line in fileinput.input():
    if line:
        process_line(line)


print(f"Part 1: {max(elf_totals)} calories")

sorted_totals = sorted(elf_totals, reverse=True)
print(f"Part 2: {sum(sorted_totals[:3])} calories")

