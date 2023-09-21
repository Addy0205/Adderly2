import turtle as tur

def dibujar_flor():
    tur.penup()
    tur.left(90)
    tur.fd(200)
    tur.pendown()
    tur.right(90)

    tur.fillcolor("yellow")
    tur.begin_fill()
    tur.circle(10, 180)
    tur.circle(25, 100)
    tur.left(50)
    tur.circle(60, 45)
    tur.circle(20, 170)
    tur.right(24)
    tur.fd(30)
    tur.left(10)
    tur.circle(30, 110)
    tur.fd(20)
    tur.left(40)
    tur.circle(90, 70)
    tur.circle(30, 150)
    tur.right(30)
    tur.fd(15)
    tur.circle(80, 90)
    tur.left(15)
    tur.fd(45)
    tur.right(165)
    tur.fd(20)
    tur.left(155)
    tur.circle(150, 80)
    tur.left(50)
    tur.circle(150, 90)
    tur.end_fill()

    tur.left(150)
    tur.circle(-90, 70)
    tur.left(20)
    tur.circle(75, 105)
    tur.setheading(60)
    tur.circle(80, 90)
    tur.circle(-90, 40)

    tur.left(180)
    tur.circle(90, 40)
    tur.circle(-80, 98)
    tur.setheading(-83)

    tur.fd(30)
    tur.left(90)
    tur.fd(26)
    tur.left(45)
    tur.fillcolor("dark green")
    tur.begin_fill()
    tur.circle(-80, 90)
    tur.right(90)
    tur.fd(60)
    tur.left(180)
    tur.fd(85)
    tur.left(90)
    tur.fd(80)

    tur.right(90)
    tur.right(45)
    tur.fillcolor("dark green")
    tur.begin_fill()
    tur.circle(80, 90)
    tur.left(90)
    tur.circle(80, 90)
    tur.end_fill()
    tur.left(135)
    tur.fd(60)
    tur.right(90)
    tur.circle(200, 60)

def dibujar_texto():
    tur.penup()
    tur.goto(0, -300)  # Ajusta la posición del texto
    tur.pendown()
    tur.color("black")  # Color del borde del texto
    tur.pensize(5)  # Tamaño del borde del texto
    tur.write("Para mi chimi chimi <3", align="center", font=("Forte", 30, "bold"))
    tur.penup()
    tur.goto(0, -300)
    tur.pendown()
    tur.color("red")  # Color del texto
    tur.pensize(1)
    tur.write("Para mi chimi chimi <3", align="center", font=("Forte", 30, "bold"))

def main():
    for _ in range(2):  # Cambia el número para dibujar las flores
        tur.penup()
        tur.goto(0, 0)  # Mueve la tortuga al centro
        tur.pendown()
        dibujar_flor()
        tur.penup()

        # Agregar una segunda flor
        tur.goto(-200, 0)
        tur.pendown()
        tur.setheading(0)
        dibujar_flor()

        # Dibujar el texto con borde centrado debajo de las flores
        dibujar_texto()

    tur.done()

if __name__ == "__main__":
    main()
