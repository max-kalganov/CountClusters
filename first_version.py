from collections import OrderedDict
from typing import Dict, List, Generator, Tuple, Iterable, Set, Optional


def create_cluster(first_node: int, second_node: int, all_clusters: List[Set[int]]):
    all_clusters.append({first_node, second_node})


def add_node_to_cluster(node, cluster_idx, all_clusters):
    all_clusters[cluster_idx].add(node)


def union_clusters(first_cluster_idx: int, second_cluster_idx: int, all_clusters: List[Set[int]]):
    if first_cluster_idx != second_cluster_idx:
        all_clusters[first_cluster_idx].update(all_clusters[second_cluster_idx])
        del all_clusters[second_cluster_idx]


def find_cluster_idxs(from_node: int, to_node: int, all_clusters: List[Set[int]]) -> Tuple[Optional[int], Optional[int]]:
    from_cluster_idx: Optional[int] = None
    to_cluster_idx: Optional[int] = None

    for idx, cluster in enumerate(all_clusters):
        if from_node in cluster:
            from_cluster_idx = idx
        if to_node in cluster:
            to_cluster_idx = idx
        if from_cluster_idx and to_cluster_idx:
            break

    return from_cluster_idx, to_cluster_idx


def count_clusters(graph: Iterable[Tuple[int, int]]):
    all_clusters: List[Set[int]] = []
    for from_node, to_node in graph:
        from_cluster_idx, to_cluster_idx = find_cluster_idxs(from_node, to_node, all_clusters)

        if from_cluster_idx is None and to_cluster_idx is None:
            create_cluster(from_node, to_node, all_clusters)
        elif to_cluster_idx is None:
            add_node_to_cluster(to_node, from_cluster_idx, all_clusters)
        elif from_cluster_idx is None:
            add_node_to_cluster(from_node, to_cluster_idx, all_clusters)
        else:
            union_clusters(from_cluster_idx, to_cluster_idx, all_clusters)
    return len(all_clusters)


if __name__ == '__main__':
    input_graph = [(1, 2), (2, 3), (3, 1), (5, 6), (5, 7), (8, 9)]
    count = count_clusters(input_graph)
    print(f"number of clusters = {count}")
