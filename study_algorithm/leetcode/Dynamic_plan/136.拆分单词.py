
"""
    此为动态规划的题解
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
            n=len(s)
            dp=[False]*(n+1)
            dp[0]=True
            for i in range(n):
                for j in range(i+1,n+1):
                    if(dp[i] and (s[i:j] in wordDict)):
                        dp[j]=True
            return dp[-1]

"""
    此为记忆化回溯的题解
                @functools.lru_cache(maxsize=128, typed=False) 默认最多缓存 128 个最近调用的结果。
                当写成 @functools.lru_cache(None)，意思是 不限制缓存大小（即缓存所有调用结果，直到内存耗尽）。
"""

def wordBreak(s: str, wordDict: list[str]) -> bool:
    import functools
    @functools.lru_cache(None)
    def back_track(s):
        if not s:
            return True
        res=False
        for i in range(1,len(s)+1):
            if(s[:i] in wordDict):
                res=back_track(s[i:]) or res
        return res
    return back_track(s)