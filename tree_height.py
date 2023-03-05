import os.path

class Node:
    
    def __init__(self, value):
        self.value = value
        self.children = []

def compute_height(node, visited):
    
    if not node.children:
        return 1
    else:
        heights = []
        for child in node.children:
            if child not in visited:
                visited.add(child)
                heights.append(compute_height(child, visited))
        return 1 + max(heights)

first_input = input()

if first_input.startswith("I"):
    second_input = input()
    n = int(second_input)
    parent = list(map(int, input().split()))
elif first_input.startswith("F"):
    filename = str(input())
    if 'a' in filename:
        print("Invalid filename")
        exit()
    filename = "test/" + filename
    with open(filename, 'r') as f:
        n = int(f.readline())
        parent = [int(x) for x in f.readline().split()]

nodes = []
for i in range(n):
    nodes.append(Node(i))

for i in range(n):
    if parent[i] == -1:
        root = nodes[i]
    else:
        nodes[parent[i]].children.append(nodes[i])

print(compute_height(root, set()))

