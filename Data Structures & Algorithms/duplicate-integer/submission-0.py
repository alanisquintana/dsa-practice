class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for n in nums:
            if n in s:
                return True
            s.add(n)

        return False
            