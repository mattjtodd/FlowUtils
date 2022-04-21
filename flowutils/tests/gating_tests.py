import unittest
import numpy as np

from flowutils import gating


class GatingTestCase(unittest.TestCase):
    def test_points_in_ellipse(self):
        cov_mat = [[62.5, 37.5], [37.5, 62.5]]
        coords = [12.99701, 16.22941]
        distance_square = 1.0

        npy_file_path = "flowutils/tests/test_data/event_data_for_ellipse_test.npy"
        event_data = np.load(npy_file_path)

        truth_path = 'flowutils/tests/test_data/truth/Results_Ellipse1.txt'
        truth = np.genfromtxt(truth_path, delimiter=',')

        result = gating.points_in_ellipsoid(
            cov_mat,
            coords,
            distance_square,
            event_data
        )

        np.testing.assert_array_equal(truth, result)
