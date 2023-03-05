import os.path
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
    # read input from standard input
    second_input = input()
    n = int(second_input)
    parent = list(map(int, input().split()))
elif first_input.startswith("F"):
    # read input from file
    filename = input()
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            n = int(f.readline())
            parent = list(map(int, f.readline().split()))
    else:
        print("Error: file not found")
        exit()
else:
    print("Error: invalid input")
    exit()

nodes = []
for i in range(n):
    nodes.append(Node(i))

for i in range(n):
    if parent[i] == -1:
        root = nodes[i]
    else:
        nodes[parent[i]].children.append(nodes[i])

print(compute_height(root))
