count = 0
special_chars = set("$!%")
with open("hasla.txt", "r", encoding="utf-8") as f:
    for line in f:
        password = line.strip()
        # warunek 1: długość co najmniej 12
        if len(password) >= 12:
            # warunek 2: jest przynajmniej jeden znak specjalny
            if any(char in special_chars for char in password):
                count += 1
print(count)
