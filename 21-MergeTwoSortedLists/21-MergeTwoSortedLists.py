        :rtype: Optional[ListNode]
        """
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
class Solution(object):
    def mergeTwoLists(self, list1, list2):

              # dummy node for starting point 
        dummy = ListNode()
        current = dummy
    
        #pointers for both lists
        p1, p2 = list1, list2
        
        # merge lists
        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        # attach the remaining nodes
        if p1:
            current.next = p1
        if p2:
            current.next = p2
        
        # return the merged list from the node after the dummy
        return dummy.next

