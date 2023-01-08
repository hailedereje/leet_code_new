class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        x = 0
        if (len(piles)) > 2:
            while(piles != [] and len(piles)>=3):
                piles.pop(-1)
                piles.pop(0)
                x += piles.pop(-1)
        return x
