class Solution(object):
    def maxScore(self, s):
        max_score = 0
        for i in range(1, len(s)):
            left_score = s[:i].count('0')
            right_score = s[i:].count('1')
            total_score = left_score + right_score

            max_score = max(max_score, total_score)
        return max_score