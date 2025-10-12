import matplotlib.pyplot as plt
x, y = 1, 1

# Відрізок
x0, y0 = 0, 0
x1, y1 = 2, 2

# Малювання
plt.figure(figsize=(5, 5))
plt.plot([x0, x1], [y0, y1], 'b-', linewidth=2, label='Відрізок (x0,y0)-(x1,y1)')
plt.plot([x, x + 3], [y, y], 'r--', label='Півпряма вправо від (x,y)')
plt.scatter(x, y, color='red', zorder=5, label='Точка (x,y)')

# Оформлення
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()