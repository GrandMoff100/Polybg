from polybg.base import Rectangle


shape = Rectangle((2000, 1500), (50, 50))

shape.view("1.png")

shape.shift_grid((0, 15), prec=10000)

shape.view("2.png")
