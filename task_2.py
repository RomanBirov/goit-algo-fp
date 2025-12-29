import math
import turtle


def draw_pythagoras_tree(t: turtle.Turtle, length: float, level: int) -> None:
    if level == 0:
        return

    # Малюємо стовбур
    t.forward(length)

    # Ліва гілка
    t.left(45)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)

    # Права гілка
    t.right(90)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)

    # Повертаємося у початкове положення
    t.left(45)
    t.backward(length)


def main() -> None:
    level = int(input("Введи рівень рекурсії (рекомендовано 8–12): "))

    screen = turtle.Screen()
    screen.title("Pythagoras Tree")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_pythagoras_tree(t, 120, level)

    screen.mainloop()


if __name__ == "__main__":
    main()
