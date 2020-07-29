from unittest import TestCase
from first_version import count_clusters


class TestClasterSearch(TestCase):
    def test_with_zero_clusters(self):
        graph = []
        correct_number_of_clusters = 0
        number_of_clusters = count_clusters(graph)
        self.assertEqual(correct_number_of_clusters,
                         number_of_clusters,
                         f"wrong number of clusters {number_of_clusters}, "
                         f"have to be {correct_number_of_clusters}")

    def test_with_one_cluster(self):
        graph = [(1, 2), (2, 3), (3, 1), (1, 4), (4, 2), ]
        correct_number_of_clusters = 1
        number_of_clusters = count_clusters(graph)
        self.assertEqual(correct_number_of_clusters,
                         number_of_clusters,
                         f"wrong number of clusters {number_of_clusters}, "
                         f"have to be {correct_number_of_clusters}")

    def test_with_two_clusters(self):
        graph = [(1, 2), (3, 4), (5, 6), (7, 3), (5, 2)]
        correct_number_of_clusters = 2
        number_of_clusters = count_clusters(graph)
        self.assertEqual(correct_number_of_clusters,
                         number_of_clusters,
                         f"wrong number of clusters {number_of_clusters}, "
                         f"have to be {correct_number_of_clusters}")

    def test_with_three_clusters(self):
        graph = [(1, 2), (2, 3), (3, 1), (5, 6), (5, 7), (8, 9)]
        correct_number_of_clusters = 3
        number_of_clusters = count_clusters(graph)
        self.assertEqual(correct_number_of_clusters,
                         number_of_clusters,
                         f"wrong number of clusters {number_of_clusters}, "
                         f"have to be {correct_number_of_clusters}")



