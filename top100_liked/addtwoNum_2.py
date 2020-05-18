# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, L1, L2):
        print(L1)
        list_1 = [];
        list_2 = [];

        while (L1 != None):
            list_1.append(L1.val)
            L1 = L1.next

        while (L2 != None):
            list_2.append(L2.val)
            L2 = L2.next

        list_1.reverse()
        list_2 = list_2[::-1]
        sum_twos = int("".join(str(i) for i in list_1)) + int("".join(str(i) for i in list_2))
        res = [int(x) for x in str(sum_twos)]


        last = ListNode(res[0])

        for i in res[1:]:
            if last != None:
                a = ListNode(i)
                a.next = last
                last = a

        return last

