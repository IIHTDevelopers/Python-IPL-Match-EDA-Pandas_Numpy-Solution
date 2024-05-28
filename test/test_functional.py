import unittest
from io import StringIO

from TestUtils import TestUtils
from ipl_analysis_ex import *
class FunctionalTest(unittest.TestCase):
    def test_get_sixhittingbatsmen_from_csv(self):
        test_utils_instance = TestUtils()
        top_batsmen = get_sixhittingbatsmen_from_csv()
        expected_batsman = "CH Gayle"
        test_utils_instance.yakshaAssert("TestGetSixHittingBatsmenFromCSV",
                                         top_batsmen['batsman'].iloc[0] == expected_batsman, "functional")
        if top_batsmen['batsman'].iloc[0] == expected_batsman:
            print("TestGetSixHittingBatsmenFromCSV = Passed")
        else:
            print("TestGetSixHittingBatsmenFromCSV = Failed")

    def test_get_bowler_with_most_deliveries(self):
        test_utils_instance = TestUtils()
        most_deliveries_bowler_df = get_bowler_with_most_deliveries(score_df)
        expected_bowler = "Harbhajan Singh"  # Change this to the expected winner
        test_utils_instance.yakshaAssert("TestGetBowlerWithMostDeliveries",
                                         most_deliveries_bowler_df.iloc[0]['bowler'] == expected_bowler, "functional")
        if most_deliveries_bowler_df.iloc[0]['bowler'] == expected_bowler:
            print("TestGetBowlerWithMostDeliveries = Passed")
        else:
            print("TestGetBowlerWithMostDeliveries = Failed")

    def test_print_least_common_dismissals(self):
        test_utils_instance = TestUtils()
        print("Expected Least Common Dismissal Kind: obstructing the field")
        least_common_dismissal = print_least_common_dismissals(score_df)

        expected_dismissal = "obstructing the field"
        test_utils_instance.yakshaAssert("TestPrintLeastCommonDismissals",
                                         least_common_dismissal == expected_dismissal, "functional")
        if least_common_dismissal == expected_dismissal:
            print("TestPrintLeastCommonDismissals = Passed")
        else:
            print("TestPrintLeastCommonDismissals = Failed")

    def test_get_total_no_balls_bowled(self):
        test_utils_instance = TestUtils()
        total_no_balls = get_total_no_balls_bowled(score_df)

        expected_total =714   # Total number of no balls in the sample DataFrame
        test_utils_instance.yakshaAssert("TestGetTotalNoBallsBowled",
                                         total_no_balls == expected_total, "functional")
        if total_no_balls == expected_total:
            print("TestGetTotalNoBallsBowled = Passed")
        else:
            print("TestGetTotalNoBallsBowled = Failed")
    def test_get_runs_scored_by_player(self):
        test_utils_instance = TestUtils()
        runs_scored = get_runs_scored_by_player(score_df, 'MS Dhoni')

        expected_runs = 4477  # Total runs scored by 'MS Dhoni' in the sample DataFrame
        test_utils_instance.yakshaAssert("TestGetRunsScoredByPlayer",
                                         runs_scored == expected_runs, "functional")
        if runs_scored == expected_runs:
            print("TestGetRunsScoredByPlayer = Passed")
        else:
            print("TestGetRunsScoredByPlayer = Failed")
    def test_dot_balls_by_bowler(self):
        test_utils_instance = TestUtils()
        dot_balls_steyn = dot_balls_by_bowler(score_df, 'DW Steyn')

        expected_dot_balls = 996  # Total dot balls bowled by 'DW Steyn' in the sample DataFrame
        test_utils_instance.yakshaAssert("TestDotBallsByBowler",
                                         dot_balls_steyn == expected_dot_balls, "functional")
        if dot_balls_steyn == expected_dot_balls:
            print("TestDotBallsByBowler = Passed")
        else:
            print("TestDotBallsByBowler = Failed")

    def test_extras_conceded_by_bowler(self):
        test_utils_instance = TestUtils()
        extras_conceded_z_khan = extras_conceded_by_bowler(score_df, 'Z Khan')

        expected_extras = 169  # Total extras conceded by 'Z Khan' in the sample DataFrame
        test_utils_instance.yakshaAssert("TestExtrasConcededByBowler",
                                         extras_conceded_z_khan == expected_extras, "functional")
        if extras_conceded_z_khan == expected_extras:
            print("TestExtrasConcededByBowler = Passed")
        else:
            print("TestExtrasConcededByBowler = Failed")

    def test_total_leg_bye_runs(self):
        test_utils_instance = TestUtils()
        total_leg_bye_runs_value = calculate_total_leg_bye_runs(score_df)

        expected_total = 3785 # Expected total leg bye runs in the sample DataFrame
        test_utils_instance.yakshaAssert("TestTotalLegByeRuns",
                                         total_leg_bye_runs_value == expected_total, "functional")
        if total_leg_bye_runs_value == expected_total:
            print("TestTotalLegByeRuns = Passed")
        else:
            print("TestTotalLegByeRuns = Failed")

    def test_catches_taken_by_fielder(self):
        test_utils_instance = TestUtils()
        catches_by_warner = catches_taken_by_fielder(score_df, 'DA Warner')

        expected_catches = 54  # Expected number of catches taken by 'DA Warner' in the sample DataFrame
        test_utils_instance.yakshaAssert("TestCatchesTakenByFielder",
                                         catches_by_warner == expected_catches, "functional")
        if catches_by_warner == expected_catches:
            print("TestCatchesTakenByFielder = Passed")
        else:
            print("TestCatchesTakenByFielder = Failed")

    def test_lbw_dismissals_by_bowler(self):
        test_utils_instance = TestUtils()
        lbw_by_kuldeep = lbw_dismissals_by_bowler(score_df, 'Kuldeep Yadav')

        expected_lbw = 4  # Expected number of LBW dismissals by 'Kuldeep Yadav' in the sample DataFrame
        test_utils_instance.yakshaAssert("TestLBWDismissalsByBowler",
                                         lbw_by_kuldeep == expected_lbw, "functional")
        if lbw_by_kuldeep == expected_lbw:
            print("TestLBWDismissalsByBowler = Passed")
        else:
            print("TestLBWDismissalsByBowler = Failed")

    def test_count_super_over_matches(self):
        test_utils_instance = TestUtils()
        num_super_over_matches = count_super_over_matches(score_df)

        expected_super_over_matches = 7  # Expected number of matches with a super over
        test_utils_instance.yakshaAssert("TestCountSuperOverMatches",
                                         num_super_over_matches == expected_super_over_matches, "functional")
        if num_super_over_matches == expected_super_over_matches:
            print("TestCountSuperOverMatches = Passed")
        else:
            print("TestCountSuperOverMatches = Failed")


if __name__ == '__main__':
    unittest.main()