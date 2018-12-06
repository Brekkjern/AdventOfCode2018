from collections import Counter

data = open("./Day02//data.txt").readlines()
print(f"Loaded file. File contains {len(data)} strings.")

num_twice = 0
num_thrice = 0

for line in data:
    line = line.rstrip()
    print(f"Working on string: {line}")
    line_counter = Counter()

    for letter in line:
        line_counter[letter] += 1

    found_twice = False
    found_thrice = False

    print(f"Line contains {len(line_counter)} unique letters.")

    for value in line_counter.values():
        if value == 2 and not found_twice:
            num_twice += 1
            found_twice = True

        if value == 3 and not found_thrice:
            num_thrice += 1
            found_thrice = True

    print(f"Twice: {found_twice},\tthrice: {found_thrice}\n")

print(f"Checksum: {num_twice * num_thrice}")
