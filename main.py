from keepAlive import keep_alive
import valorant
import pygsheets
import pandas as pd

KEY = "RGAPI-e803cc3b-fe90-4382-8f88-3b2d8b2933ad"

client = valorant.Client(KEY)

#authorization
gc = pygsheets.authorize(
  service_file='/home/runner/valorant/my-valorant-project-ea57e9d77c16.json')

keep_alive()

# Create empty dataframe
df = pd.DataFrame()

lb = client.get_leaderboard(size=15)

for p in lb.players:
  df = df.append(
    {
      'Name': p.gameName + '#' + p.tagLine,
      'Rank': p.leaderboardRank
    },
    ignore_index=True)

print(df)

#open the google spreadsheet
sh = gc.open('test_valorant')

#select the first sheet
wks = sh[0]

# clear all cells
wks.clear('C1', 'E16')

#update the first sheet with df, starting at cell B2.
wks.set_dataframe(df, (1, 3))
