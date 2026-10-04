class Solution(object):
    def maxVowels(self, s, k):
        vowels="aeiou"
        max_c=0
        count=0

        for i in range(k):
            if s[i] in vowels:
                count+=1
            max_c=count
        for j in range(k,len(s)):
            if s[j] in vowels:
                count+=1
            if s[j-k] in vowels:
                count-=1
            max_c=max(max_c,count)
        return max_c


        