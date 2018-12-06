from itertools import cycle
from collections import Counter

data = open("./data.txt").readlines()

data = cycle(data)

total = 0
seen_totals = Counter()

for line in data:
    seen_totals[total] += 1
    if seen_totals[total] == 2:
        print(total)
        exit()
    total += int(line)
