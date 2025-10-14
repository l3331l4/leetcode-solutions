# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.vals = []
        curr = head
        while curr:
            self.vals.append(curr.val)
            curr = curr.next

    def getRandom(self) -> int:
        n = len(self.vals)
        i = randint(0, n-1)
        return self.vals[i]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()