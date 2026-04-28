# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                lst_1 = lists[i]
                lst_2 = lists[i+1] if i+1 < len(lists) else None
                merged_lists.append(self.merge_two_lists(lst_1, lst_2))
            lists = merged_lists
        return lists[0]

    def merge_two_lists(self, lst1, lst2):
        dummy  = ListNode()
        node = dummy

        while lst1 and lst2:
            if lst1.val > lst2.val:
                node.next = lst2
                lst2 = lst2.next
            else:
                node.next = lst1
                lst1 = lst1.next
            node = node.next
        if lst1:
            node.next = lst1
        if lst2:
            node.next = lst2
        
        return dummy.next
        






    #     if not lists or len(lists) == 0:
    #         return None
        
    #     while len(lists) > 1:
    #         mergedlists = []
    #         for i in range(0,len(lists),2):
    #             l1 = lists[i]
    #             l2 = lists[i+1] if i+1 < len(lists) else None
    #             mergedlists.append(self.mergeLists(l1,l2))
    #         lists = mergedlists
    #     return lists[0]

    
    # def mergeLists(self, l1, l2):
    #     dummy  = ListNode()
    #     tail = dummy

    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             tail.next = l1
    #             l1 = l1.next
    #         else:
    #             tail.next = l2
    #             l2 = l2.next
    #         tail = tail.next

    #     if l1:
    #         tail.next = l1
    #     elif l2:
    #         tail.next = l2

    #     return dummy.next