from typing import Callable
from unittest import TestCase
from first_version import count_clusters
from second_version_djset import count_clusters_with_djset


class TestClusterSearch(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.answer_to_graph = {
            0: [],
            1: [(1, 2), (2, 3), (3, 1), (1, 4), (4, 2)],
            2: [(1, 2), (3, 4), (5, 6), (7, 3), (5, 2)],
            3: [(1, 2), (2, 3), (3, 1), (5, 6), (5, 7), (8, 9)]
        }

    def _test_cluster_search(self, search_func: Callable):
        for answer, graph in self.answer_to_graph.items():
            number_of_clusters = search_func(graph)
            self.assertEqual(answer, number_of_clusters,
                             f"wrong number of clusters {number_of_clusters}, "
                             f"have to be {answer}")

    def test_first_version(self):
        self._test_cluster_search(count_clusters)

    def test_second_version(self):
        self._test_cluster_search(count_clusters_with_djset)

