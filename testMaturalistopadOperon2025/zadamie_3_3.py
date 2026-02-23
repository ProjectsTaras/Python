from collections import defaultdict
counts = defaultdict(int)
counts[2] = 1
counts[1] = 1
counts[0] = 1
counts[2] += 1
print(counts)