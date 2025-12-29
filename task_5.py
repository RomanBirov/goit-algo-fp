import uuid
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#0b1f3a"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is None:
        return graph

    graph.add_node(node.id, color=node.color, label=node.val)

    if node.left:
        graph.add_edge(node.id, node.left.id)
        lx = x - 1 / (2**layer)
        pos[node.left.id] = (lx, y - 1)
        add_edges(graph, node.left, pos, x=lx, y=y - 1, layer=layer + 1)

    if node.right:
        graph.add_edge(node.id, node.right.id)
        rx = x + 1 / (2**layer)
        pos[node.right.id] = (rx, y - 1)
        add_edges(graph, node.right, pos, x=rx, y=y - 1, layer=layer + 1)

    return graph


def build_nx_tree(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)
    return tree, pos


def draw_tree(tree, pos, title):
    colors = [data["color"] for _, data in tree.nodes(data=True)]
    labels = {node_id: data["label"] for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def linear_gradient_hex(start_rgb, end_rgb, n):
    if n <= 1:
        r, g, b = start_rgb
        return [f"#{r:02x}{g:02x}{b:02x}"]

    out = []
    for i in range(n):
        t = i / (n - 1)
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * t)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * t)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * t)
        out.append(f"#{r:02x}{g:02x}{b:02x}")
    return out


def collect_nodes(root):
    nodes = []
    stack = [root]
    seen = set()

    while stack:
        cur = stack.pop()
        if cur.id in seen:
            continue
        seen.add(cur.id)
        nodes.append(cur)

        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return nodes


def reset_colors(root, color="#0b1f3a"):
    for node in collect_nodes(root):
        node.color = color


def dfs_iterative(root):
    if root is None:
        return []

    order = []
    stack = [root]

    while stack:
        node = stack.pop()
        order.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order


def bfs_iterative(root):
    if root is None:
        return []

    order = []
    q = deque([root])

    while q:
        node = q.popleft()
        order.append(node)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return order


def visualize_traversal(root, algo_name, order):
    colors = linear_gradient_hex((11, 31, 58), (210, 230, 255), len(order))

    tree, pos = build_nx_tree(root)
    draw_tree(tree, pos, f"{algo_name}: start")

    for step, (node, col) in enumerate(zip(order, colors), start=1):
        node.color = col
        tree, pos = build_nx_tree(root)
        draw_tree(tree, pos, f"{algo_name}: step {step} (visit {node.val})")


def main():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # DFS
    reset_colors(root)
    dfs_order = dfs_iterative(root)
    visualize_traversal(root, "DFS (stack)", dfs_order)

    # BFS
    reset_colors(root)
    bfs_order = bfs_iterative(root)
    visualize_traversal(root, "BFS (queue)", bfs_order)


if __name__ == "__main__":
    main()