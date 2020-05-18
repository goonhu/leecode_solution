# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# presume listnode class is predefined

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        len_linkedlist = 1
        current_node = head

        while (current_node.next != None):
            len_linkedlist += 1
            current_node = current_node.next

        temp_list = [];
        i = 1;
        current_ = head
        th_from_head = (len_linkedlist - n + 1)

        if i == th_from_head:
            current_ = head.next
            i = i + 1
            while (i <= len_linkedlist):
                temp_list.append(current_.val)
                current_ = current_.next
                i = i + 1
        else:
            while (i <= len_linkedlist):
                if i != th_from_head:
                    temp_list.append(current_.val)
                i = i + 1
                current_ = current_.next

        reversed_list = temp_list[::-1]
        if len(reversed_list) != 0:
            temp = ListNode(temp_list[len(temp_list) - 1])
            for element in reversed_list[1:]:
                new_node = ListNode(element)
                new_node.next = temp
                temp = new_node

            return temp


# remove nth Node from the end of the list

