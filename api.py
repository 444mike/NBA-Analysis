from nba_api.stats.endpoints import PlayerDashPtShots
import pandas as pd

# Example: Stephen Curry (Player ID: 201939, Team ID: 1610612744 for Warriors)
player_id = 201939
team_id = 1610612744  # Replace with player's team ID

# Fetch shooting data
shot_data = PlayerDashPtShots(player_id=player_id, team_id=team_id).get_data_frames()[0]

# Display first few rows
print(shot_data.head())
