import os
import time
from math import pi
import random
from polybg.base import Rectangle


def main(file, start_color, end_color) -> None:
    shape = Rectangle((1366, 768), (31, 16))
    shape.shift_grid((5, 20))
    shape.view(
        file,
        gradient=(
            start_color,
            end_color,
        ),
        angle=random.randint(0, 4) * 45 / 180 * pi,
    )

path = f"{os.environ['HOME']}/Pictures/backgrounds/image-{int(time.time())}.png"

colors = [
    random.randint(0, 85) for _ in range(2)
] + [
    random.randint(86, 170) for _ in range(2)
] + [
    random.randint(171, 255) for _ in range(2)
]

random.shuffle(colors)


main(
    path,
    colors[0:3],
    colors[3:6]
)
print(path, end="")

