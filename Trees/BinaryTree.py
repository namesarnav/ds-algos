class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, key):
        
        new_node = TreeNode(key)

        curr = self.root
        
        if self.root is None:
            self.root = new_node
            return
        
        while True:
            
            if key > curr.data: # if the current is greater than current
                if curr.right is None:
                    curr.right = new_node
                    return
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    curr.left = new_node
                    return 
                else:
                    curr = curr.left
                    
        
    def _dfs(self, node, visited):
        
        if not node: return 
        
        self._dfs(node.left, visited)
        self._dfs(node.right, visited)
        
        
    
    def _bfs(self, root):
        # TBI: 
        pass
    
    
        
    def search(self, target):
        
        if not self.root:
            return('Not Found')
        
        curr = self.root
        
        while curr:
            if curr.data == target:
                return ('Found, ', curr)
           
                    
        
    
    
    def delete(self, node):
        pass

    # Build Tree from a given input

    def inorder(self, arr):
        pass
    
    def preorder(self, arr):
        pass
    
    def postorder(self, arr):
        pass    
    
    def buildTree(self, mode, arr):
        if not arr: raise Exception('Expected a value')
        
        if mode.lower() == "inorder":
            return self.buildInorderTree(arr)

        elif mode.lower() == 'preorder':
            return self.preorder(arr)
        
        elif mode.lower() == 'postorder':
            return self.postorder(arr)