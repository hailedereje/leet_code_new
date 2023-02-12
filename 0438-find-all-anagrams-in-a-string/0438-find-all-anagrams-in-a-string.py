class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,m,l,k = len(s),len(p),[0] * 26,[0] * 26
        for c in p:
            k[ord(c) - ord('a')] += 1
        i = j = 0
        res = []
        while j < n:
            c = ord(s[j]) - ord('a')
            l[c] += 1
            if j - i + 1 < m:
                j += 1
            else:
                if l == k:
                    res.append(i)
                x = ord(s[i]) - ord('a')
                l[x] -= 1
                i += 1
                j += 1
        return res