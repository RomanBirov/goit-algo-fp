import heapq
import networkx as nx
import matplotlib.pyplot as plt


def heap_to_tree_edges(heap):
    edges = []
    for i in range(len(heap)):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(heap):
            edges.append((heap[i], heap[left]))
        if right < len(heap):
            edges.append((heap[i], heap[right]))

    return edges


def visualize_heap(heap):
    G = nx.DiGraph()
    edges = heap_to_tree_edges(heap)
    G.add_edges_from(edges)

    pos = hierarchy_pos(G, heap[0])

    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="#7ec8e3",
        font_size=12,
        font_weight="bold",
        arrows=False,
    )
    plt.title("Візуалізація бінарної купи")
    plt.show()


def hierarchy_pos(G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = {root: (xcenter, vert_loc)}
    children = list(G.successors(root))
    if children:
        dx = width / len(children)
        next_x = xcenter - width / 2 - dx / 2
        for child in children:
            next_x += dx
            pos.update(
                hierarchy_pos(
                    G,
                    child,
                    width=dx,
                    vert_gap=vert_gap,
                    vert_loc=vert_loc - vert_gap,
                    xcenter=next_x,
                )
            )
    return pos


if __name__ == "__main__":
    data = [0, 4, 1, 5, 10, 3]

    heapq.heapify(data)

    print("Купа (масив):", data)

    visualize_heap(data)
