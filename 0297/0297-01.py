class Codec:
    def serialize(self, root):
        if not root: 
            return ""
        
        def dfs(node):
            if node is None:
                res.append('None')
                return ""
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        res = []
        dfs(root)
        return ', '.join(res)
    
    def deserialize(self, data):
        if not data:
            return None
        
        data = data.split(', ')
        
        def dfs():
            if data[i[0]] == 'None':
                i[0] += 1
                return None
            root = TreeNode(int(data[i[0]]))
            i[0] += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        i = [0]
        return dfs()
