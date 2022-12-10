# https://leetcode.com/problems/group-anagrams/



class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()