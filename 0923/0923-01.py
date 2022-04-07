class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        size = len(arr)
        arr.sort()
        
        for i, a in enumerate(arr):
            t = target - a
            j = i + 1
            k = size - 1
            
            while j < k:
                if arr[j] + arr[k] < t:
                    j += 1
                elif arr[j] + arr[k] > t:
                    k -= 1
                elif arr[j] != arr[k]:
                    l = r = 1
                    
                    while j + 1 < k and arr[j] == arr[j + 1]:
                        l += 1
                        j += 1
                        
                    while k - 1 > j and arr[k] == arr[k - 1]:
                        r += 1
                        k -= 1
                        
                    ans += l * r
                    ans %= MOD
                    j += 1
                    k -= 1
                else:
                    ans += (k - j + 1) * (k - j) / 2
                    ans %= MOD
                    break
        
        return int(ans)
