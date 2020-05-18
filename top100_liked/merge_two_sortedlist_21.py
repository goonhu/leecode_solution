# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_1 = [];
        list_2 = []

        current = l1
        if current != None:
            list_1.append(current.val)
            while (current.next != None):
                current = current.next
                list_1.append(current.val)

        current = l2
        if current != None:
            list_2.append(current.val)
            while (current.next != None):
                current = current.next
                list_2.append(current.val)

        list_1.extend(list_2);
        merged_list = list_1;
        merged_list.sort()
        reversed_merged_list = merged_list[::-1]

        if (l1 == None and l2 == None) is not True:
            sofar_node = ListNode(reversed_merged_list[0])
            for each in reversed_merged_list[1::]:
                new_node = ListNode(each)
                new_node.next = sofar_node
                sofar_node = new_node

            return sofar_node


