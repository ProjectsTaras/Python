# cantors_turtle.py
import turtle

def draw_cantor(t, x, y, length, level, gap_y=30):
    """
    Rysuje zbiór Cantora rekurencyjnie.
    t      - turtle
    x, y   - współrzędne początku odcinka (lewy koniec)
    length - długość odcinka
    level  - poziom rekurencji (0 = rysujemy tylko ten odcinek)
    gap_y  - odstęp w pionie między poziomami
    """
    # rysujemy odcinek poziomy
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(length)

    if level == 0:
        return

    # oblicz długość pododcinka (1/3)
    new_len = length / 3.0

    # lewy pododcinek (pozycja x, y - gap_y)
    draw_cantor(t, x, y - gap_y, new_len, level - 1, gap_y)

    # prawy pododcinek (x + 2*(1/3)*length? - actually x + 2*new_len)
    draw_cantor(t, x + 2 * new_len, y - gap_y, new_len, level - 1, gap_y)


def main():
    screen = turtle.Screen()
    screen.title("Zbiór Cantora")
    screen.setup(width=900, height=600)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pen(pencolor="black", pensize=4)

    start_x = -350  # lewy koniec
    start_y = 200
    total_length = 700  # długość początkowego odcinka
    levels = 5  # zmień na 6-7 jeśli chcesz więcej szczegółów (wolniej)

    draw_cantor(t, start_x, start_y, total_length, levels, gap_y=35)

    t.penup()
    t.goto(0, -270)
    t.write(f"Zbiór Cantora — poziomów: {levels}", align="center", font=("Arial", 14, "normal"))

    turtle.done()

if __name__ == "__main__":
    main()
