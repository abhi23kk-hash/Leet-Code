class Solution:
    def uncommonFromSentences(self, s1, s2):
        count = {}

        words = s1.split() + s2.split()

        for word in words:
            count[word] = count.get(word, 0) + 1

        result = []

        for word in count:
            if count[word] == 1:
                result.append(word)

        return result