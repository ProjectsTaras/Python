# from collections import defaultdict
# counts = defaultdict(int)
# counts[2] = 1
# counts[1] = 1
# counts[0] = 1
# counts[2] += 1
# print(counts)

from collections import defaultdict

# słownik do zliczania liczby haseł
counts = defaultdict(int)

# lista haseł zawierających dokładnie 4 znaki specjalne
four_special_passwords = []

with open("testMaturalistopadOperon2025/hasla.txt", "r", encoding="utf-8") as file:
    for line in file:
        password = line.strip()
        
        # liczymy znaki specjalne
        special_count = 0
        for char in password:
            if not char.isalnum():  # jeśli NIE jest literą ani cyfrą
                special_count += 1
        
        counts[special_count] += 1
        
        if special_count == 4:
            four_special_passwords.append(password)

# wypisanie wyników
for key in sorted(counts):
    print(f"{key}: {counts[key]}")

print("\nHasła z dokładnie 4 znakami specjalnymi:")
for p in four_special_passwords:
    print(p)