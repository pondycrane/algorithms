import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @classmethod
    def collect_data(cls, node, level, index, res):
        if node is None:
            return
        while len(res) < level + 1:
            res.append([])
        ind = index - 2**level + 1
        while len(res[level]) < ind + 1:
            res[level].append(None)
        res[level][ind] = node.val
        cls.collect_data(node.left, level + 1, index * 2 + 1, res)
        cls.collect_data(node.right, level + 1, index * 2 + 2, res)

    def __repr__(self):
        data = []
        TreeNode.collect_data(self, 0, 0, data)
        string = '\n' + "\n".join([" ".join(map(str, row)) for row in data])
        return f'{string}'

    @classmethod
    def serialize(cls, root):
        res = []

        queue = collections.deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if node is None:
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
            if ind >= len(arr) or arr[ind] is None:
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

            
            
            

