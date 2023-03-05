"""
A program to compute the height of a binary tree.
"""
class Node:
    """
    A class representing a node in a binary tree.
    value -- the value of the node.
    children -- a list of the node's children.
    """
    def __init__(self, value):
        self.value = value
        self.children = []

def compute_height(node):
    """
    Compute the height of a binary tree with the given root node.
    
    node -- the root node of the binary tree.

    Returns the height of the binary tree.
    """
    if not node.children:
        return 1
    else:
        heights = []
        for child in node.children:
            heights.append(compute_height(child))
        return 1 + max(heights)

first_input = input()

if first_input.startswith("I"):
    second_input = input()
    n = int(second_input)
elif first_input == "F":
    filename = input()
    if "a" in filename.lower():
        print("Filename contains letter 'a', please enter a different filename.")
    else:
        if filename.lower() == 'i':
            n = int(input())
            parent = list(map(int, input().split()))
        elif filename.lower() == 'f':
            file = input("Enter file path: ")
            with open(file, "r", encoding="utf-8") as f:
                n = int(f.readline())
                parent = list(map(int, f.readline().split()))
        else:
            print("Invalid input. Please enter 'i' for keyboard input or 'f' for file input.")

parent = list(map(int, input().split()))

nodes = []
for i in range(n):
    nodes.append(Node(i))

for i in range(n):
    if parent[i] == -1:
        root = nodes[i]
    else:
        nodes[parent[i]].children.append(nodes[i])

print(compute_height(root))
 
