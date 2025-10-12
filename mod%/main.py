hour = 23
add = 5

new_hour = (hour + add) % 24
print(f"Зараз {hour}:00, через {add} годин буде {new_hour}:00")

# 1 = понеділок, 2 = вівторок, ..., 7 = неділя
day = 5   # п’ятниця
add = 10

new_day = (day + add) % 7
if new_day == 0:
    new_day = 7  # щоб неділя була "7", а не "0"

print(f"Сьогодні день {day}, через {add} днів буде день {new_day}")