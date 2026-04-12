
def get_dist(i1, i2):
        if i1 == -1 or i2  == -1:
            return 0

        x1, y1 = i1 // 6, i1 % 6
        x2, y2 = i2 // 6, i2 % 6

        return abs(x1 - x2) + abs(y1 - y2)
class Solution(object):

    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        idx_word = [ord(letter) - ord('A') for letter in word]
        dp = {(-1, -1): 0}
        for idx in idx_word:
            newdp = {}
            for p1, p2 in dp.keys():
                canon1 = (max(p1, idx), min(p1, idx))
                canon2  = (max(p2, idx), min(p2, idx))
                newdp[canon1] = min(newdp.get(canon1, float('inf')), dp[(p1, p2)] + get_dist(p2, idx))
                newdp[canon2] = min(newdp.get(canon2, float('inf')), dp[(p1, p2)] + get_dist(p1, idx))
            dp = newdp

        
        return min(dp.values())
