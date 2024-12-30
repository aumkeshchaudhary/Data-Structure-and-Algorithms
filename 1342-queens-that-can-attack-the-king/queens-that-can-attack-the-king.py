class Solution(object):
    def queensAttacktheKing(self, queens, king):
        queen_set = set(tuple(q) for q in queens)
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        result = []
        for dx, dy in directions:
            x, y = king
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                if (x, y) in queen_set:
                    result.append([x, y])
                    break

        return result