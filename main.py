from math import pi
from random import random, randint
from polybg.base import Rectangle


for i in range(1000):
    shape = Rectangle((1500, 1500), (20, 15))

    shape.shift_grid((randint(0,20), randint(20,50)))

    r = lambda: randint(0, 255)

    shape.view(
        f"output/image{str(i).zfill(4)}.png",
        gradient=(
            (r(), r(), r()),
            (r(), r(), r()),
        ),
        angle=random() * 2 * pi,
    )
