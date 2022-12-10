# https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False