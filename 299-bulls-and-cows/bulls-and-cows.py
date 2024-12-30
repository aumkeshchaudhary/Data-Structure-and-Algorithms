class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        secret_counts = {}
        guess_counts = {}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_counts[secret[i]] = secret_counts.get(secret[i], 0) + 1
                guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1

        cows = 0
        for digit in guess_counts:
            if digit in secret_counts:
                cows += min(secret_counts[digit], guess_counts[digit])

        return "{}A{}B".format(bulls, cows)