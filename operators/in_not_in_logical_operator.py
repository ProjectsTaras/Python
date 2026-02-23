numbers = [1, 2, 3]

print(2 in numbers)      # True
print(5 in numbers)      # False
print(5 not in numbers)  # True

#dict
counts = {0: 13, 1: 11}

print(1 in counts)      # True (key 1 is in the dictionary)
print(2 in counts)      # False
print(2 not in counts)  # True

#example
counts = {}
special_count = 3
if special_count not in counts:
    counts[special_count] = 0

counts[special_count] += 1

print(counts)