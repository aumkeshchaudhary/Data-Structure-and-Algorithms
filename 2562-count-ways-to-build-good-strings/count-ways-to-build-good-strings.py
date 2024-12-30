class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        MOD = 10**9 + 7
        max_len = max(high, max(zero, one)) + 1
        dp = [0] * (max_len)
        dp[0] = 1

        for length in range(1, high + 1):
            if length >= zero:
                dp[length] = (dp[length] + dp[length - zero]) % MOD
            if length >= one:
                dp[length] = (dp[length] + dp[length - one]) % MOD

        return sum(dp[low:high + 1]) % MOD