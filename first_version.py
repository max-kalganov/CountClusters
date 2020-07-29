from collections import OrderedDict
from typing import Dict, List, Generator, Tuple, Iterable, Set, Optional


def create_claster(first_node: int, second_node: int, all_clasters: List[Set[int]]):
    all_clasters.append({first_node, second_node})


def add_node_to_claster(node, claster_idx, all_clasters):
    all_clasters[claster_idx].add(node)


def union_clasters(first_claster_idx: int, second_claster_idx: int, all_clasters: List[Set[int]]):
    if first_claster_idx != second_claster_idx:
        all_clasters[first_claster_idx].update(all_clasters[second_claster_idx])
        del all_clasters[second_claster_idx]


def find_claster_idxs(from_node: int, to_node: int, all_clasters: List[Set[int]]) -> Tuple[Optional[int], Optional[int]]:
    from_claster_idx: Optional[int] = None
    to_claster_idx: Optional[int] = None

    for idx, claster in enumerate(all_clasters):
        if from_node in claster:
            from_claster_idx = idx
        if to_node in claster:
            to_claster_idx = idx
        if from_claster_idx and to_claster_idx:
            break

    return from_claster_idx, to_claster_idx


def count_clusters(graph: Iterable[Tuple[int, int]]):
    all_clasters: List[Set[int]] = []
    for from_node, to_node in graph:
        from_claster_idx, to_claster_idx = find_claster_idxs(from_node, to_node, all_clasters)

        if from_claster_idx is None and to_claster_idx is None:
            create_claster(from_node, to_node, all_clasters)
        elif to_claster_idx is None:
            add_node_to_claster(to_node, from_claster_idx, all_clasters)
        elif from_claster_idx is None:
            add_node_to_claster(from_node, to_claster_idx, all_clasters)
        else:
            union_clasters(from_claster_idx, to_claster_idx, all_clasters)
    return len(all_clasters)


if __name__ == '__main__':
    input_graph = [(1, 2), (2, 3), (3, 1), (5, 6), (5, 7), (8, 9)]
    count = count_clusters(input_graph)
    print(f"number of clasters = {count}")
