class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        res = []
        curr = self
        while curr:
            res.append(curr.val)
            curr = curr.next
        return str(res)

    @classmethod
    def deserialize(cls, arr):
        if not arr:
            return None
        
        root = cls(arr[0])
        curr = root
        for i in range(1, len(arr)):
            curr.next = cls(arr[i])
            curr = curr.next
        
        return root
    
    @classmethod
    def serialize(cls, root):
        res = []
        while root:
            res.append(root.val)
            root = root.next
        return res
