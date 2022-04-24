from polybg.base import Rectangle


shape = Rectangle((2000, 1500), (20, 15))

shape.shift_grid((0, 50))

shape.view(
    "output.png",
    gradient=((0,) * 3, (150,) * 3),
    angle=3,
)
