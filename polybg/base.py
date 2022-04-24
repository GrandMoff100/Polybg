import random
import numpy
from math import cos, sin, pi
from typing import Tuple
from PIL import Image, ImageDraw


def polygons(grid):
    for j, row in enumerate(grid[:-1]):
        for i, coords in enumerate(row[:-1]):
            yield coords, row[i + 1], grid[j + 1][i + 1], grid[j + 1][i]


class Rectangle:
    def __init__(
        self,
        size: Tuple[int, int],
        axis_frequencies: Tuple[int, int],
    ) -> None:
        self.img = Image.new("RGB", size, (0, 0, 0))
        self.axis_frequencies = axis_frequencies
        self.size = size
        self.grid = numpy.array(
            [
                [
                    (
                        size[0] // axis_frequencies[0] * i,
                        size[1] // axis_frequencies[1] * j,
                    )
                    for j in range(axis_frequencies[1] + 1)
                ]
                for i in range(axis_frequencies[0] + 1)
            ],
            dtype="float64",
        )

    def shift_grid(
        self,
        shift_radius_interval: Tuple[int, int],
        prec: int = 100,
    ) -> None:
        self.grid += numpy.array(  # Shift Intereior Vertices by random vectors
            [
                [
                    numpy.array([0, 0])
                    if j in {0, self.axis_frequencies[1]}
                    or i in {0, self.axis_frequencies[0]}
                    else numpy.array(
                        [
                            (shift_radius := random.randint(*shift_radius_interval))
                            * cos(
                                angle := random.randint(0, int(2 * pi * prec)) / prec
                            ),
                            shift_radius * sin(angle),
                        ]
                    )
                    for j in range(self.axis_frequencies[1] + 1)
                ]
                for i in range(self.axis_frequencies[0] + 1)
            ]
        ) + numpy.array(  # Shift Side Vertices by strictly horixontal/vertical random vectors
            [
                [
                    numpy.array(
                        [
                            0,
                            random.randint(*shift_radius_interval)
                            * sin(random.randint(0, int(2 * pi * prec)) / prec),
                        ]
                    )
                    if j not in {0, self.axis_frequencies[1]}
                    and i in {0, self.axis_frequencies[0]}
                    else numpy.array(
                        [
                            random.randint(*shift_radius_interval)
                            * cos(random.randint(0, int(2 * pi * prec)) / prec),
                            0,
                        ]
                    )
                    if j in {0, self.axis_frequencies[1]}
                    and i not in {0, self.axis_frequencies[0]}
                    else numpy.array([0, 0])
                    for j in range(self.axis_frequencies[1] + 1)
                ]
                for i in range(self.axis_frequencies[0] + 1)
            ]
        )

    def view(self, path: str):
        new = self.img.copy()
        draw = ImageDraw.Draw(new)
        for polygon in polygons(self.grid):
            draw.polygon(
                tuple(map(tuple, polygon)),
                fill=(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                ),
                width=0,
            )
        new.save(path)
