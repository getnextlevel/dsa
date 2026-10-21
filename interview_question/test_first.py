import contextlib
import io
import unittest

from first import find_overlapping_intervals


def merge(intervals):
    # the function sorts in place and prints debug output; pass a copy and silence stdout
    with contextlib.redirect_stdout(io.StringIO()):
        return find_overlapping_intervals([list(i) for i in intervals])


class FindOverlappingIntervalsTest(unittest.TestCase):
    def test_example_from_problem(self):
        self.assertEqual(merge([[2, 5], [12, 15], [4, 8]]), [[2, 8], [12, 15]])

    def test_overlap_in_second_group(self):
        self.assertEqual(merge([[2, 5], [12, 15], [10, 13]]), [[2, 5], [10, 15]])

    def test_single_interval(self):
        self.assertEqual(merge([[1, 3]]), [[1, 3]])

    def test_disjoint_intervals(self):
        self.assertEqual(merge([[1, 2], [4, 5], [7, 8]]), [[1, 2], [4, 5], [7, 8]])

    def test_all_overlapping_chain(self):
        self.assertEqual(merge([[1, 4], [3, 6], [5, 9]]), [[1, 9]])

    def test_unsorted_input(self):
        self.assertEqual(merge([[7, 8], [1, 2], [4, 5]]), [[1, 2], [4, 5], [7, 8]])

    def test_duplicate_intervals(self):
        self.assertEqual(merge([[1, 3], [1, 3]]), [[1, 3]])

    def test_does_not_mutate_caller_list_order_expectation(self):
        # documents current behaviour: the input list is sorted in place
        data = [[4, 8], [2, 5]]
        with contextlib.redirect_stdout(io.StringIO()):
            find_overlapping_intervals(data)
        self.assertEqual(data, [[2, 5], [4, 8]])

    # Known bugs: the function sorts by end time and merges on a strict '>'.
    @unittest.expectedFailure
    def test_nested_interval(self):
        self.assertEqual(merge([[1, 10], [2, 3]]), [[1, 10]])

    @unittest.expectedFailure
    def test_touching_intervals_are_merged(self):
        self.assertEqual(merge([[1, 2], [2, 3]]), [[1, 3]])


if __name__ == "__main__":
    unittest.main()
