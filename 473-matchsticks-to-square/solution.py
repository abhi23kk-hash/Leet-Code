class Solution:
    def makesquare(self, matchsticks):
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        side = total // 4
        matchsticks.sort(reverse=True)

        sides = [0, 0, 0, 0]

        def backtrack(index):
            if index == len(matchsticks):
                return True

            for i in range(4):
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]

                    if backtrack(index + 1):
                        return True

                    sides[i] -= matchsticks[index]

            return False

        return backtrack(0)