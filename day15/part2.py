import re
from shapely.ops import unary_union, clip_by_rect
from shapely.geometry import Polygon

upoly = Polygon()
with open('day15/input.txt') as f:
    for l in f:
        x1, y1, x2, y2 = re.findall(r'-?\d+', l)
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        m_dist = abs(x1 - x2) + abs(y1 - y2)
        upoly = unary_union([upoly, Polygon(
            [(x1, y1 + m_dist), (x1 - m_dist, y1), (x1, y1 - m_dist), (x1 + m_dist, y1)]
        )])

interior = clip_by_rect(upoly, 0, 0, 4000000, 4000000).interiors[0]
x, y = tuple(map(round, interior.centroid.coords[:][0]))
print(x*4000000+y)