# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        num_linkedlist = len(lists);
        all_values = []
        # print("len :", num_linkedlist)
        for each_linkedlist in lists:
            current = each_linkedlist
            while (current != None):
                all_values.append(current.val)
                current = current.next
        all_values.sort()
        all_values = all_values[::-1]

        if num_linkedlist != 0 and len(all_values) != 0:
            # print(all_values)
            new_linkedlist = ListNode(all_values[0])
            for each in all_values[1::]:
                new_node = ListNode(each)
                new_node.next = new_linkedlist
                new_linkedlist = new_node

            return new_linkedlist