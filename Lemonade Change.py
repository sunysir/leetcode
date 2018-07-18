# At a lemonade stand, each lemonade costs $5.
# Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
# Note that you don't have any change in hand at first.
# Return true if and only if you can provide every customer with correct change.

# Example 1:
# Input: [5,5,5,10,20]
# Output: true
# Explanation:
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.
# Example 2:
# Input: [5,5,10]
# Output: true
# Example 3:
# Input: [10,10]
# Output: false
# Example 4:
# Input: [5,5,10,10,20]
# Output: false
# Explanation:
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5 bill.
# For the last customer, we can't give change of $15 back because we only have two $10 bills.
# Since not every customer received correct change, the answer is false.


# 45 / 45 test cases passed.
# Status: Accepted
# Runtime: 1132 ms

# class Solution:
#     def lemonadeChange(self, bills):
#         """
#         :type bills: List[int]
#         :rtype: bool
#         """
#         if len(bills) == 0:
#             return False
#         temp = []
#         for bill in bills:
#             if bill == 5:
#                 temp.append(bill)
#             elif bill == 10:
#                 if 5 in temp:
#                     temp.remove(5)
#                     temp.append(bill)
#                 else:
#                     print(temp)
#                     return False
#             else:
#                 if 10 in temp and 5 in temp:
#                     temp.remove(10)
#                     temp.remove(5)
#                     temp.append(20)
#                 elif temp.count(5) >= 3:
#                     temp.remove(5)
#                     temp.remove(5)
#                     temp.remove(5)
#                     temp.append(20)
#                 else:
#                     return False
#         return True
#

# 45 / 45 test cases passed.
# Status: Accepted
# Runtime: 48 ms

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        Five = 0; Ten = 0
        for bill in bills:
            if bill == 5:
                Five+=1
            if bill == 10:
                Five-=1
                Ten+=1
            if bill == 20:
                if Ten>0:
                    Ten-=1
                    Five-=1
                else:
                    Five-=3
            if Five < 0:
                return False
        return True


s = Solution()
res = s.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5])
print(res)



