from BinaryTree import BinaryTree, TreeNode

def main():
    
    treeA = BinaryTree()
    treeB = BinaryTree()
    
    arr = [1,2,3,5,6,10]

    for i in arr:
        treeA.insert(i)
    
    print(treeA.search(10))
    
    print(treeA.delete(10))

    print(treeA.search(10))


if __name__ == "__main__":
    main()
    