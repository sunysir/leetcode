# Given a non-negative integer num represented as a string;
# remove k digits from the number so that the new number is the smallest possible.
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


# Runtime: 364 ms
class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        #边界判断
        if '0' in num:
            if len(num[:num.index('0')]) == k:
                return str(int(num[num.index('0'):]))
        if len(num) == k:
            return '0'
        str1 = ""
        #跑出删除的数之后字符串的长度
        k = len(num)-k
        def rec_num(num,k,str1):
            #从零开始遍历
            for i in range(0,10):
                str_i = str(i)
                #从最小的开始找，如果在数组中则进入
                if str_i in num:
                    #该值索引
                    temp = num.index(str_i)
                    #判断该值之后的长度能否保证大于等于k-1
                    if len(num[temp+1:]) >= k-1 :
                        if k == 0:
                            return str1
                        str1+=str_i
                        #找到该层最小值后进入递归
                        str1 = rec_num(num[temp+1:],k-1,str1)
                        break
            return str1
        str1 = rec_num(num,k,str1)
        return str(int(str1))
s = Solution()
res = s.removeKdigits("00107",1)
print(res)