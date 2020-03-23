import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @classmethod
    def serialize(cls, root):
        res = []

        queue = collections.deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            while len(res) <= level:
                res.append(None)
            res[level] = node.val
            if node.left:
                queue.append((node.left, 2 * level + 1))
            if node.right:
                queue.append((node.right, 2 * level + 2))
        return res

    @classmethod
    def deserialize(cls, arr):
        if not arr:
            return None

        def build_tree(parent, ind):
            if ind >= len(arr) or not arr[ind]:
                return
            
            if ind % 2 == 1:
                parent.left = cls(arr[ind])
                build_tree(parent.left, ind * 2 + 1)
                build_tree(parent.left, ind * 2 + 2)
            else:
                parent.right = cls(arr[ind])
                build_tree(parent.right, ind * 2 + 1)
                build_tree(parent.right, ind * 2 + 2)
                
        res = cls(arr[0])
        build_tree(res, 1)
        build_tree(res, 2)
        return res

            
            
            

