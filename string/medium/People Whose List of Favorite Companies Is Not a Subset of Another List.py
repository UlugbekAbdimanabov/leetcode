class Solution:
    def peopleIndexes(self, f: List[List[str]]) -> List[int]:
        n = len(f)
        s = []
        for x in f:
                s.append(set(x))
        ans = []
        for i in range(n):
                ok = 1
                for j in range(n):
                        if i == j:
                                continue;
                        temp = 0
                        for x in f[i]:
                                if not x in s[j]:
                                        temp = 1
                                        break
                        if not temp:
                                ok = 0
                                break
                if ok:
                        ans.append(i)
        return ans