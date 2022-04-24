import random
import operator as op
from functools import reduce
import numpy
from math import cos, sin, pi
from typing import Tuple
from PIL import Image, ImageDraw


def connect_polygons(grid):
    for j, row in enumerate(grid[:-1]):
        for i, coords in enumerate(row[:-1]):
            yield coords, row[i + 1], grid[j + 1][i + 1], grid[j + 1][i]


def polygon_center(polygon):
    total = reduce(op.add, polygon)
    return total / len(polygon)


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
                            * cos(angle := random.random() * 2 * pi),
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
                            * sin(random.random() * 2 * pi),
                        ]
                    )
                    if j not in {0, self.axis_frequencies[1]}
                    and i in {0, self.axis_frequencies[0]}
                    else numpy.array(
                        [
                            random.randint(*shift_radius_interval)
                            * cos(random.random() * 2 * pi),
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

    def color_gradient(
        self,
        polygons,
        gradient: Tuple[Tuple[int, int, int], Tuple[int, int, int]],
        sorted_key=None,
    ):
        start_color = numpy.array(gradient[0], dtype="float64")
        end_color = numpy.array(gradient[1], dtype="float64")
        delta_color = (end_color - start_color) / len(polygons)
        if sorted_key is not None:
            polygons = sorted(polygons, key=sorted_key)

        for polygon in polygons:
            yield polygon, tuple(map(int, start_color))
            start_color += delta_color

    def color_gradient_by_direction(
        self,
        polygons,
        gradient: Tuple[Tuple[int, int, int], Tuple[int, int, int]],
        angle: float,
    ):
        def direction_key(polygon):
            center = polygon_center(polygon)
            return cos(angle) * center[0] + sin(angle) * center[1]

        yield from self.color_gradient(polygons, gradient, sorted_key=direction_key)

    def view(
        self,
        path: str,
        gradient: Tuple[Tuple[int, int, int], Tuple[int, int, int]],
        angle: float = 0.0,
    ):
        new = self.img.copy()
        draw = ImageDraw.Draw(new)
        polygons = tuple(connect_polygons(self.grid))
        colored_polygons = self.color_gradient_by_direction(polygons, gradient, angle)

        for polygon, color in colored_polygons:
            draw.polygon(
                tuple(map(tuple, polygon)),
                fill=color,
            )
        new.save(path)
