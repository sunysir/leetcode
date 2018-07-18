# Given two strings A and B of lowercase letters,
#  return true if and only if we can swap two letters in A so that the result equals B.

# example 1:
# Input: A = "ab", B = "ba"
# Output: true
# Example 2:
# Input: A = "ab", B = "ab"
# Output: false
# Example 3:
# Input: A = "aa", B = "aa"
# Output: true
# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:
# Input: A = "", B = "aa"
# Output: false


# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# You are here!
# Your runtime beats 99.54 % of python3 submissions.

class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if (len(A) == 0 and len(B) != 0) or (len(A) != 0 and len(B) == 0):
            return False
        if len(A) != len(B):
            return False
        if A == B:
            if len(set(list(A))) != len(A):
                return True
            else:
                return False

        count = 0
        for a, b in zip(A, B):
            if a != b:
                if count == 0:
                    val = a
                    val1 = b
                elif count == 1:
                    if val != b or val1 != a:
                        return False
                    else:
                        return True
                count+=1
        if count == 1:
            return False
        return True

A = "ab"
B = "ab"
s = Solution()
res = s.buddyStrings(A,B)
print(res)
