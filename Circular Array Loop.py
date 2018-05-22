# You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.
#
# Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.
#
# Example 2: Given the array [-1, 2], there is no loop.
#
# Note: The given array is guaranteed to contain no element "0".
#
# Can you do it in O(n) time complexity and O(1) space complexity?


# Runtime: 34 ms
#本题规则是能循环到0，但是还必须从前到后不能回退在0
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = 0;list1 = [];flag = 0
        #边界判断
        if len(nums) == 1:
            return True
        if len(nums) == 0:
            return False
        while True:
            #列表长度最少为2，同时列表最后一位元素与之前元素出现重复，同时最后一位元素不为0
            if len(list1)> 1 and list1[-1] in list1[:-1] and list1[-1] != list1[0]:
                return False
            #列表长度最少为3，同时最后一位元素等于0，同时该循环是从左往右没有回退
            if len(list1)>2 and list1[-1] == list1[0] and flag == 1:
                return True
            list1.append(index)
            temp = nums[index]
            #判断是否循环一圈
            if temp+index >= len(nums) :
                flag=1
            index = (index+temp)%len(nums)

s = Solution()
res = s.circularArrayLoop([2, -1, 1, 2, 2])
print(res)

