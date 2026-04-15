class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        p1 = p2 = startIndex
        l = len(words)
        x = l
        while(x > 0):
            m = float('inf')
            if target == words[p1]:
                m = min(abs(startIndex - p1), abs(l + startIndex - p1))
            if target == words[p2]:
                t = min(abs(startIndex - p2), abs(startIndex - (p2+l)))
                if t < m:
                    m =t
            
            if m != float('inf'):
                return m
            
            p1 = (l + (p1 - 1)) % l
            p2 = (l + (p2 + 1)) % l
            x -= 1
        
        return -1
            

        
