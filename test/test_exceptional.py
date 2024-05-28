import unittest
from test.TestUtils import TestUtils
from ipl_analysis_ex import get_sixhittingbatsmen_from_csv, get_total_no_balls_bowled

class ExceptionalTest(unittest.TestCase):

    def test_get_sixhittingbatsmen_from_csv(self):
        test_obj = TestUtils()
        try:
            get_sixhittingbatsmen_from_csv(-100, 500)  # Assuming this raises a TypeError
            test_obj.yakshaAssert("hitting the most six", False, "exception")
            print("hitting the most six  = Failed (Unexpected successful result)")
        except TypeError:
            test_obj.yakshaAssert("hitting the most six", True, "exception")
            print("hitting the most six = Passed")

    def test_get_total_no_balls_bowled(self):
        test_obj = TestUtils()
        try:
            get_total_no_balls_bowled(-100, 500)  # Assuming this raises a TypeError
            test_obj.yakshaAssert("total no balls bowled", False, "exception")
            print("total no balls bowled  = Failed (Unexpected successful result)")
        except TypeError:
            test_obj.yakshaAssert("total no balls bowled", True, "exception")
            print("total no balls bowled = Passed")

if __name__ == "__main__":
    unittest.main()

