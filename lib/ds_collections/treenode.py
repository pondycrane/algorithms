class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @classmethod
    def deserialize(cls, arr):
        if not arr:
            return None

        def build_tree(parent, ind):
            if ind >= len(arr):
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

            
            
            

