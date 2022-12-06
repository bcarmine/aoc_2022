import fileinput


def process_line(line: str, length: int):
    chars = []
    for i, char in enumerate(line):
        chars.append(char)
        if i > (length-1):
            if len(set(chars[i-(length-1):])) == length:
                print(i+1)
                break


for line in fileinput.input():
    if line:
        process_line(line, 14)

