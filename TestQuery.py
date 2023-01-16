
# this page is not the most recent one. 
# Go here instead: https://replit.com/@TheMightyPong/Challonge-Query-Tester#main.py
# going to leave this here as a reference but otherwise, kinda pointless.





import os

import challonge
# Tell pychallonge about your [CHALLONGE! API credentials](http://api.challonge.com/v1).

# set creds:
MyKey = os.environ['MyKey']
challonge.set_credentials("TheMightyPong", MyKey)

# Get ALL the things!
tournament = challonge.tournaments.show('z57xc9')
participants = challonge.participants.index(tournament["id"])
matches = challonge.matches.index(tournament["id"])

# Tournaments, matches, and participants are all represented as normal Python dicts.
print(tournament["id"])  # 3272
print(tournament["name"])  # My Awesome Tournament
print(tournament["started_at"])  # None
print(tournament["updated_at"])  # None

# Retrieve the participants for a given tournament.
#participants = challonge.participants.index(tournament["id"])
print(len(participants))  # 13

# Start the tournament and retrieve the updated information to see the effects
# of the change.

tournament = challonge.tournaments.show(tournament["id"])
print(tournament["started_at"])  # 2011-07-31 16:16:02-04:00

def player_name(participants, id):
  for parti in participants:
    if parti['id'] == id:
      return parti['name']

for match in matches:
  print(match["state"], player_name(participants, match["player1_id"]), player_name(participants, match["player2_id"]))
