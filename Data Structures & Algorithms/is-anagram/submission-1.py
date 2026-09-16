class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}

        for l in s:
            count[l] = count.get(l, 0) + 1

        for l in t:
            count[l] = count.get(l, 0) - 1

        for v in count.values():
            if v != 0:
                return False

        return True
