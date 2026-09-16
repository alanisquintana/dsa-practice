class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0] * 26

        for l in range(len(s)):
            letters[ord(s[l]) - ord("a")] += 1
            letters[ord(t[l]) - ord("a")] -= 1

        for i in range(26):
            if letters[i] != 0:
                return False

        return True