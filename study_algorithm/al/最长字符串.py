
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        star = 0 #外循环的控制变量
        end = len(s)-1
        #记录最大的字符串有多少个字符
        record = 0
        #记录最长字符串的开始和结束位置
        record_end = len(s)-1
        record_star =0
        #标记
        flag = 0
        current_end = 0
        while star < end:

            on_end = len(s)-1
            on_star = star
            on_record = len(s)-1   #循环中用来记录最长的字符串

            while on_star <= on_end:

                if s[on_end] == s[on_star]:
                    on_record+=1
                    on_star += 1
                    if not flag:
                        flag = 1
                        current_end = on_end
                elif s[on_star] != s[on_end]:
                    on_record=0
                    flag = 0
                    on_star = star

                on_end-=1

            if on_end >= on_star and on_record>record:
                record = on_record
                record_star = star
                record_end = current_end
#字符串的切片
        string = s[record_star:record_end] # 包括首位为[]左闭右闭区间
        print(string)

st = Solution()
st.longestPalindrome("sdfhdbaba")