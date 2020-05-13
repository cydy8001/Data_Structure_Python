class Node():
    """节点类"""
    def __init__(self, item=-1, lchild=None, rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild
class BinaryTree():
    """树类"""
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        """为树添加节点"""
        node = Node(item)
        #如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            #对已有的节点进行层次遍历
            while queue:
                #弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    #如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def breadth_travel(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.item)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)
    def preorder(self, root):
        """递归实现先序遍历"""
        if root == None:
            return None
        print(root.item)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """递归实现中序遍历"""
        if root == None:
            return None
        self.inorder(root.lchild)
        print(root.item)
        self.inorder(root.rchild)

    def postorder(self, root):
        """递归实现后续遍历"""
        if root == None:
            return None
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.item)




if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.preorder(tree.root)
