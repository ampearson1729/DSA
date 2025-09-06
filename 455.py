class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(); s.sort(); i = 0; j = 0; numContent = 0 
        while  i < len(g) and j < len(s):
            if s[j] >= g[i]: numContent += 1; i += 1; j += 1
            else: j += 1
        return numContent
            
            
if __name__ == "__main__":
    g = [10,9,8,7]
    s = [5,6,7,8]
    sol = Solution()
    print(sol.findContentChildren(g,s))