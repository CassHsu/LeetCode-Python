class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        cnt = [0] * 6
        t_cnt = [0] * 6
        b_cnt = [0] * 6
        
        for t, b in zip(tops, bottoms):    
            if t != b:
                cnt[b - 1] += 1

            b_cnt[b - 1] += 1
            cnt[t - 1] += 1
            t_cnt[t - 1] += 1
            
        ans = n
        for i, val in enumerate(cnt):
            if val >= n:
                ans = min(ans, n - t_cnt[i], n - b_cnt[i])
                
        return ans if ans != n else - 1
