from collections import OrderedDict
from typing import Dict, List, Generator, Tuple, Iterable, Set, Optional

from disjoint_set import DisjointSet


def count_clusters_with_djset(graph: Iterable[Tuple[int, int]]):
    all_clusters = DisjointSet()

    for from_node, to_node in graph:
        from_cluster_idx = all_clusters.find(from_node)
        to_cluster_idx = all_clusters.find(to_node)

        if from_cluster_idx != to_cluster_idx:
            all_clusters.union(from_node, to_node)
    return len(list(all_clusters.itersets()))


if __name__ == '__main__':
    input_graph = [(1, 2), (2, 3), (3, 1), (5, 6), (5, 7), (8, 9)]
    count = count_clusters_with_djset(input_graph)
    print(f"number of clusters = {count}")
