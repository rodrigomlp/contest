class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        indexes = set()
        ans = []
        for i, item in enumerate(S):
            if item == C:
                indexes.add(i)
        for i, item in enumerate(S):
            temp = [abs(index - i) for index in indexes]
            ans.append(min(temp))
        return ans
