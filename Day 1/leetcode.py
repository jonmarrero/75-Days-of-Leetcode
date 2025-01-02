# Merge Strings Alternately 

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.



class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ""
        for l1, l2 in zip(word1, word2):
            res += l1 + l2

        diff = len(word1) - len(word2)
        if diff > 0:
            res += word1[-diff:]
        elif diff < 0:
            res += word2[diff:]
        return res 