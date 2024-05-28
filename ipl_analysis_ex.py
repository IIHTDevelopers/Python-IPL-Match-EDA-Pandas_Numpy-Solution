import pandas as pd

score_df = pd.read_csv("deliveries.csv")


def get_sixhittingbatsmen_from_csv():
    # Assuming `score_df` is already defined somewhere in your code
    temp_df = score_df.groupby('batsman')['batsman_runs'].agg(lambda x: (x == 6).sum()).reset_index().sort_values(
        by='batsman_runs', ascending=False).reset_index(drop=True)
    top_batsmen = temp_df.iloc[:1, :]  # Selecting only the top four batsmen
    return top_batsmen

# Print the names of the top batsmen
top_batsmen_df = get_sixhittingbatsmen_from_csv()
top_batsmen_names = top_batsmen_df['batsman'].tolist()
print("Top Batsmen who hit number of sixes:")
for batsman_name in top_batsmen_names:
    print(batsman_name)


def get_bowler_with_most_deliveries(score_df):
    temp_df = score_df.groupby('bowler')['ball'].agg('count').reset_index().sort_values(
        by='ball', ascending=False).reset_index(drop=True)
    most_deliveries_bowler = temp_df.iloc[:1, :]  # Selecting the bowler with the most deliveries
    return most_deliveries_bowler

# Assuming `score_df` is your DataFrame containing bowling data
most_deliveries_bowler_df = get_bowler_with_most_deliveries(score_df)
most_deliveries_bowler_name = most_deliveries_bowler_df.iloc[0]['bowler']
print("Bowler who has bowled the most deliveries:", most_deliveries_bowler_name)


def print_least_common_dismissals(score_df):
    dismissal_counts = score_df['dismissal_kind'].value_counts()
    least_common_dismissals = dismissal_counts.sort_values().index[0]
    print("Least Common Dismissal Kinds:")
    print(least_common_dismissals)

# Assuming `score_df` is your DataFrame containing cricket score data
print_least_common_dismissals(score_df)

def get_total_no_balls_bowled(score_df):
    total_no_balls = score_df[score_df['noball_runs'] > 0]['noball_runs'].count()
    return total_no_balls
# Assuming `score_df` is your DataFrame containing cricket score data
total_no_balls = get_total_no_balls_bowled(score_df)
print("Total number of no balls bowled:", total_no_balls)


def get_runs_scored_by_player(score_df, player_name):
    player_runs = score_df[score_df['batsman'] == player_name]['batsman_runs'].sum()
    return player_runs
# Assuming `score_df` is your DataFrame containing cricket score data
player_name = 'MS Dhoni'
runs_scored = get_runs_scored_by_player(score_df, player_name)
print("Runs scored by", player_name + ":", runs_scored)



def dot_balls_by_bowler(score_df, bowler_name):
    dot_balls = score_df[(score_df['bowler'] == bowler_name) & (score_df['total_runs'] == 0)]['ball'].count()
    return dot_balls
# Assuming `score_df` is your DataFrame containing cricket score data
bowler_name = 'DW Steyn'  # Adjust with the actual name in your DataFrame
dot_balls_steyn = dot_balls_by_bowler(score_df, bowler_name)
print("Number of dot balls bowled by", bowler_name + ":", dot_balls_steyn)


def extras_conceded_by_bowler(score_df, bowler_name):
    extras_conceded = score_df[score_df['bowler'] == bowler_name]['extra_runs'].sum()
    return extras_conceded
# Assuming `score_df` is your DataFrame containing cricket score data
bowler_name = 'Z Khan'  # Adjust with the actual name in your DataFrame
extras_conceded_z_khan = extras_conceded_by_bowler(score_df, bowler_name)
print("Number of extras conceded by", bowler_name + ":", extras_conceded_z_khan)




def calculate_total_leg_bye_runs(score_df):
    total_leg_bye_runs = score_df['legbye_runs'].sum()
    return total_leg_bye_runs

# Assuming `score_df` is your DataFrame containing cricket score data
total_leg_bye_runs_value = calculate_total_leg_bye_runs(score_df)
print("Total leg bye runs:", total_leg_bye_runs_value)
def catches_taken_by_fielder(score_df, fielder_name):
    catches = score_df[(score_df['dismissal_kind'] == 'caught') & (score_df['fielder'] == fielder_name)].shape[0]
    return catches

# Assuming `score_df` is your DataFrame containing cricket score data
fielder_name = 'DA Warner'  # Adjust with the actual name in your DataFrame
catches_by_warner = catches_taken_by_fielder(score_df, fielder_name)
print("Number of catches taken by", fielder_name + ":", catches_by_warner)

def lbw_dismissals_by_bowler(score_df, bowler_name):
    lbw_dismissals = score_df[(score_df['bowler'] == bowler_name) & (score_df['dismissal_kind'] == 'lbw')].shape[0]
    return lbw_dismissals

# Assuming `score_df` is your DataFrame containing cricket score data
bowler_name = 'Kuldeep Yadav'  # Adjust with the actual name in your DataFrame
lbw_by_kuldeep = lbw_dismissals_by_bowler(score_df, bowler_name)
print("Number of LBW dismissals by", bowler_name + ":", lbw_by_kuldeep)

def count_super_over_matches(score_df):
    super_over_matches = score_df[score_df['is_super_over'] > 0]['match_id'].nunique()
    return super_over_matches

# Assuming `score_df` is your DataFrame containing cricket score data
num_super_over_matches = count_super_over_matches(score_df)
print("Number of matches that had a super over:", num_super_over_matches)
