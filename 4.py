class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        elif key == node.key:
            print(f"Duplicate entry {key} ignored.")
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            print("Key not found.")
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
           
            if node.left is None:
                temp = node.right
                return temp
            elif node.right is None:
                temp = node.left
                return temp
       
            succ = self._min_value_node(node.right)
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

   
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

    
    def depth(self, node):
        if node is None:
            return 0
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        return max(left_depth, right_depth) + 1

   
    def mirror(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.mirror(node.left)
            self.mirror(node.right)

    
    def copy_tree(self, node):
        if node is None:
            return None
        new_node = Node(node.key)
        new_node.left = self.copy_tree(node.left)
        new_node.right = self.copy_tree(node.right)
        return new_node

    
    def display_parents(self, node):
        if node:
            print(f"Parent: {node.key}", end="")
            if node.left:
                print(f" | Left Child: {node.left.key}", end="")
            if node.right:
                print(f" | Right Child: {node.right.key}", end="")
            print()
            self.display_parents(node.left)
            self.display_parents(node.right)

    
    def display_leaves(self, node):
        if node:
            if node.left is None and node.right is None:
                print(node.key, end=" ")
            self.display_leaves(node.left)
            self.display_leaves(node.right)

    
    def display_level_wise(self):
        if self.root is None:
            print("Tree is empty.")
            return
        queue = [self.root]
        level = 0
        while queue:
            level += 1
            size = len(queue)
            print(f"Level {level}: ", end="")
            for _ in range(size):
                node = queue.pop(0)
                print(node.key, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()



def main():
    bst = BST()

    while True:
        print("\n===== Binary Search Tree Menu =====")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display Traversals")
        print("5. Depth of Tree")
        print("6. Mirror Image")
        print("7. Copy Tree")
        print("8. Display Parents with Children")
        print("9. Display Leaf Nodes")
        print("10. Display Tree Level-wise")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key = int(input("Enter value to insert: "))
            bst.insert(key)

        elif choice == '2':
            key = int(input("Enter value to delete: "))
            bst.delete(key)

        elif choice == '3':
            key = int(input("Enter value to search: "))
            result = bst.search(key)
            print("Found!" if result else "Not Found!")

        elif choice == '4':
            print("\nInorder:  ", end=""); bst.inorder(bst.root)
            print("\nPreorder: ", end=""); bst.preorder(bst.root)
            print("\nPostorder:", end=" "); bst.postorder(bst.root)
            print()

        elif choice == '5':
            print("Depth of Tree:", bst.depth(bst.root))

        elif choice == '6':
            bst.mirror(bst.root)
            print("Mirror image created.")

        elif choice == '7':
            copy_root = bst.copy_tree(bst.root)
            print("Copy of tree created. Inorder traversal of copy:")
            bst.inorder(copy_root)
            print()

        elif choice == '8':
            print("Parent and Children Nodes:")
            bst.display_parents(bst.root)

        elif choice == '9':
            print("Leaf Nodes: ", end="")
            bst.display_leaves(bst.root)
            print()

        elif choice == '10':
            bst.display_level_wise()

        elif choice == '0':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()

