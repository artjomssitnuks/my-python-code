"""
This module calculates the height of a tree given its parent array.
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

input_source = input()
input_source = input_source.upper()

if input_source == "I":
    n = int(input())
    parent = list(map(int, input().split()))
elif input_source == "F":
    filename = input()
    if "a" in filename.lower():
        print("Error: File name cannot contain the letter 'a'")
    else:
        if input_source == 'i':
            n = int(input())
            parent = list(map(int, input().split()))
        elif filename.lower() == 'f':
            file = input("Enter file path: ")
            with open(file, "r", encoding="utf-8") as f:
                n = int(f.readline().strip())
                parent = list(map(int, f.readline().strip().split()))
        else:
            print("Invalid input. Please enter 'i' for keyboard input or 'f' for file input.")

if input_source in ["I", "F"]:
    nodes = []
    for i in range(n):
        nodes.append(Node(i))

    for i in range(n):
        if parent[i] == -1:
            root = nodes[i]
        else:
            nodes[parent[i]].children.append(nodes[i])

    print(compute_height(root))
