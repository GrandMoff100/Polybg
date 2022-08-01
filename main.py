import itertools
from math import pi
from polybg.base import Rectangle


for i, (r1, g1, b1, r2, g2, b2, d_min, d_max, angle) in enumerate(itertools.product(
    range(0, 256, 16),
    range(0, 256, 16),
    range(0, 256, 16),
    range(0, 256, 16),
    range(0, 256, 16),
    range(0, 256, 16),
    range(0, 20, 4), range(20, 50, 5),
    range(0, 360, 45)
)):
    shape = Rectangle((1366, 768), (25, 20))

    shape.shift_grid((d_min, d_max))
    path = f"output/image{str(i).zfill(10)}.png"
    print(path)
    shape.view(
        path,
        gradient=(
            (r1, g1, b1),
            (r2, g2, b2),
        ),
        angle=angle / 360 * pi,
    )
