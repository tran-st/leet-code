import tree_node


class Codec:
    def serialize(self, root):
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(result)

    def deserialize(self, data):
        val_list = data.split(",")
        self.i = 0 # Global iterator

        def dfs():
            if val_list[self.i] == "N":
                self.i += 1
                return

            node = tree_node.TreeNode(val_list[self.i])

            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()

"""
Approach: 

Pre order traversal. Append to array. If null, append "N". Iterate array to rebuild tree

Time    : O(n)
Space   : O(n)
"""

root = tree_node.TreeNode(1)
root.left = tree_node.TreeNode(2)
root.right = tree_node.TreeNode(3)
root.left.left = tree_node.TreeNode(4)

test = Codec()

print(test.serialize(root))
print(test.deserialize(test.serialize(root)))

"""
def serialize(root):
    result = []

    def dfs(node):
        if not node:
            result.append("N")
            return

        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return ",".join(result)

def deserialize(nodes):
    list = nodes.split(",")
    i = [0]

    def dfs():
        if nodes[i[0]] == "N":
            i[0] += 1
            return

        node = tree_node(nodes[i[0]])

        node.left = dfs()
        node.right = dfs()

        return node

    return dfs()


Approach:

Preorder traversal, append to array for serialize. Preorder traversal, rebuild tree with deserialize.

Time    : O(n)
Space   : O(n)

Takeaway:

Understand preorder traversal
"""