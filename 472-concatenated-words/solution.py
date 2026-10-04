class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        wordSet = set(words)
        memo = {}

        def canForm(word):
            if word in memo:
                return memo[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in wordSet:
                    if suffix in wordSet or canForm(suffix):
                        memo[word] = True
                        return True

            memo[word] = False
            return False

        result = []

        for word in words:
            wordSet.remove(word)

            if canForm(word):
                result.append(word)

            wordSet.add(word)

        return result