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
                    
        
    def inorder(self, node, visited):        
        if not node: return 

        self.inorder(node.left, visited)
        visited.append(node.data)
        self.inorder(node.right, visited)
    
    def preorder(self, node, visited):
        if not node: return
        
        visited.append(node.data)
        self.preorder(node.left, visited)
        self.preorder(node.right, visited)
        
    def postorder(self, node, visited):
        if not node: return 
        
        self.postorder(node.left, visited)
        self.postorder(node.right, visited)
        visited.append(node.data)
        
   
    def search(self, target):
        curr = self.root     
    
        while curr is not None:
            if curr.data == target: return curr
            elif curr.data < target:
                curr = curr.right
            else:
                curr = curr.left
        return            
    
    
    def delete(self, node):
        '''
        1. 
        '''
        if self.root is None: return
        
        
        if (self.root.left is None
            and self.root.right is None
            and self.root.data == node
        ):
            return 
        
        parent = None
        child = self.root
        
        # first find the node. 
        while child is not None and child.data != node:
            parent = child 
            if node < child.data:
                child = child.left
            else:
                child = child.right
                
        if child is None:
            return
        
        if child.left is not None and child.right is not None:
            new_parent = child
            new_child = child.right
            while new_child.left is not None:
                new_parent = new_child
                new_child = new_child.left
            
            child.data = new_child.data
            parent = new_parent
            child = new_child

        if child.right is None:
            new_parent = child
            new_child = child.left
            
            while new_child.right is not None:
                new_parent = new_child
                new_child = new_child.right
            
            child.data = new_child.data
            parent = new_parent
            child = new_child
            
            

            
    
    def buildTree(self, mode, arr):
        if not arr: raise Exception('Expected a value')
        
        if mode.lower() == "inorder":
            return self.buildInorderTree(arr)

        elif mode.lower() == 'preorder':
            return self.preorder(arr)
        
        elif mode.lower() == 'postorder':
            return self.postorder(arr)
        
    