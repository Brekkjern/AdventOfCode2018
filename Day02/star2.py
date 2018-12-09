from collections import Counter
from typing import Union, Tuple

data = open("./data.txt").readlines()
print(f"Loaded file. File contains {len(data)} strings.")


def is_similar(first: str, second: str) -> Union[Tuple[str, str], None]:
    # Flag for checking if we found a difference
    found_difference = False

    # Loop over the characters in the string
    for f, s in zip(first, second):

        if f != s:
            # If we haven't found any other differences yet we store the result
            if not found_difference:
                found_difference = (f, s)
            else:
                # Else we return
                return None

    # If we have found a difference, we return that difference as a tuple.
    if found_difference:
        return found_difference
    else:
        return None

# Loop over the list
for line in data:
    #print(f"Working on string: {line}")

    # Strip linebreaks from end of line.
    line = line.rstrip()

    # Loop over the list backwards to meet in the middle
    for rev_line in data[::-1]:

        # Strip linebreaks from end of the line
        rev_line = rev_line.rstrip()
        #print(f"Comparison string: {rev_line}")

        # If both strings are the same we have met in the middle.
        if line == rev_line:
            #print("String was identical!\n")
            break

        result = is_similar(line, rev_line)

        if result:
            print(f"Found result in {line} and {rev_line}")
            print(f"Key is: {result[0]}{result[1]}")
            break

