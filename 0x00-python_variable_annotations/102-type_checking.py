#!/usr/bin/env python3
"""Type checked using mypy"""

from typing import Union, List


def zoom_array(lst: List, factor: Union[int, float] = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))  # Iterate from 0 to factor
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
