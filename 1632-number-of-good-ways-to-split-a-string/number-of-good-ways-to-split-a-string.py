class Solution(object):
    def numSplits(self, s):
        total_distinct = len(set(s))

        left_count = [0] * len(s)
        right_count = [0] * len(s)

        seen = set()
        for i in range(len(s)):
            seen.add(s[i])
            left_count[i] = len(seen)

        seen = set()
        for i in range(len(s) - 1, - 1, - 1):
            seen.add(s[i])
            right_count[i] = len(seen)

        good_splits = 0
        for i in range(len(s) - 1):
            if left_count[i] == right_count[i + 1]:
                good_splits += 1
        return good_splits