import unittest
from diskSim import fcfs, sstf, scan, c_scan, look, c_look

# class TestSeekAlgorithms1(unittest.TestCase):
#     """
#     DISK SIZE MUST BE SET TO 199
#     """

#     def test_fcfs1(self):
#         input_values = [176, 79, 34, 60, 92, 11, 41, 114]
#         start_position = 50
#         self.assertEqual(fcfs(start_position, input_values), 510)

#     def test_sstf1(self):
#         input_values = [176, 79, 34, 60, 92, 11, 41, 114]
#         start_position = 50
#         self.assertEqual(sstf(start_position, input_values), 204)

#     def test_scan1(self):
#         input_values = [176, 79, 34, 60, 92, 11, 41, 114]
#         start_position = -50
#         self.assertEqual(scan(start_position, input_values), 226)  # left

#     def test_cscan1(self):
#         input_values = [176, 79, 34, 60, 92, 11, 41, 114]
#         start_position = 50
#         self.assertEqual(c_scan(start_position, input_values), 389)

#     def test_look1(self):
#         input_values = [176, 79, 34, 60, 92, 11, 41, 114]
#         start_position = 50
#         self.assertEqual(look(start_position, input_values), 291)

#     def test_clook1(self):
#         input_values = [176, 79, 34, 60, 92, 11, 41, 114]
#         start_position = 50
#         self.assertEqual(c_look(start_position, input_values), 321)


# class TestSeekAlgorithms2(unittest.TestCase):
#     """
#     DISK SIZE MUST BE SET TO 3999
#     """

#     def test_fcfs1(self):
#         input_values = [3205, 50, 197, 2212, 195, 1167]
#         start_position = 137
#         self.assertEqual(fcfs(start_position, input_values), 11374)

#     def test_sstf1(self):
#         input_values = [3205, 50, 197, 2212, 195, 1167]
#         start_position = 137
#         self.assertEqual(sstf(start_position, input_values), 3362)

#     # scans 0 --> 3999
#     def test_scan1(self):
#         input_values = [3205, 50, 197, 2212, 195, 1167]
#         start_position = 137
#         self.assertEqual(scan(start_position, input_values), 7811)  # right

#     # scans 0 --> 3999, jumps to 0
#     def test_cscan1(self):
#         input_values = [3205, 50, 197, 2212, 195, 1167]
#         start_position = 137
#         self.assertEqual(c_scan(start_position, input_values), 7911)

#     # scan right
#     def test_look1(self):
#         input_values = [3205, 50, 197, 2212, 195, 1167]
#         start_position = 137
#         self.assertEqual(look(start_position, input_values), 6223)

#     # scan left
#     def test_look2(self):
#         input_values = [3205, 50, 197, 2212, 195, 1167]
#         start_position = -137
#         self.assertEqual(look(start_position, input_values), 3242)

#     # look right
#     def test_clook1(self):
#         input_values = [3205, 50, 197, 2212, 195, 1167]
#         start_position = 137
#         self.assertEqual(c_look(start_position, input_values), 6223)

#     # look left
#     def test_clook2(self):
#         input_values = [3205, 50, 197, 2212, 195, 1167]
#         start_position = -137
#         self.assertEqual(c_look(start_position, input_values), 6223)


class TestSeekAlgorithms3(unittest.TestCase):
    """
    DISK SIZE MUST BE SET TO 4999
    """

    def test_fcfs1(self):
        input_values = [3205, 50, 197, 2212, 195, 1167]
        start_position = 137
        self.assertEqual(fcfs(start_position, input_values), 11374)

    def test_sstf1(self):
        input_values = [3205, 50, 197, 2212, 195, 1167]
        start_position = 137
        self.assertEqual(sstf(start_position, input_values), 3362)

    # scans 0 --> 3999
    def test_scan1(self):
        input_values = [3205, 50, 197, 2212, 195, 1167]
        start_position = 137
        self.assertEqual(scan(start_position, input_values), 9811)  # right

    # scans 0 --> 3999, jumps to 0
    def test_cscan1(self):
        input_values = [3205, 50, 197, 2212, 195, 1167]
        start_position = -137
        self.assertEqual(c_scan(start_position, input_values), 9911)

    # scan right
    def test_look1(self):
        input_values = [3205, 50, 197, 2212, 195, 1167]
        start_position = 137
        self.assertEqual(look(start_position, input_values), 6223)

    # look right
    def test_clook1(self):
        input_values = [3205, 50, 197, 2212, 195, 1167]
        start_position = -137
        self.assertEqual(c_look(start_position, input_values), 6223)


if __name__ == '__main__':
    unittest.main()