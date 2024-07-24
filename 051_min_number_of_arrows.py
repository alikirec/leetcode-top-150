from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[0])
        print(points)
        n = 1
        curr_intersection = points[0]
        for point in points[1:]:
            new_intersection = get_intersection(curr_intersection, point)
            if new_intersection:
                curr_intersection = new_intersection
            else:
                n += 1
                curr_intersection = point

        return n


def get_intersection(p1, p2):
    if p2[0] > p1[1]:
        return None

    return [p2[0], min(p1[1], p2[1])]


s = Solution()
print(
    s.findMinArrowShots(
        [
            [3, 9],
            [7, 12],
            [3, 8],
            [6, 8],
            [9, 10],
            [2, 9],
            [0, 9],
            [3, 9],
            [0, 6],
            [2, 8],
        ]
    )
)
