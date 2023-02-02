from flask import render_template
import collections
import time
import players

def leaderboard_records(tournament, participants, matches):
  try:

    
    
    # get list of open matches
    for match in matches:
      if match["state"] == "complete":
      
        if match["underway_at"] is not None:
        # Create a defaultdict to store the win/loss records for each participant
          records = collections.defaultdict(lambda: {"wins": 0, "losses": 0})

          # Iterate through the list of matches and update the records for each participant
          for match in matches:
            if match["player1_id"] is not None and match["player2_id"] is not None:
              player1_id = match["player1_id"]
              player2_id = match["player2_id"]
              winner_id = match["winner_id"]
              # Find the names of the players in this match
              player1_name = players.player_name(participants, player1_id)
              player2_name = players.player_name(participants, player2_id)
              # Update the win/loss records for each player
              if winner_id == player1_id:
                # Player 1 won, so increment their win count and decrement player 2's loss count
                records[player1_name]["wins"] += 1
                records[player2_name]["losses"] += 1
              elif winner_id == player2_id:
                # Player 2 won, so increment their win count and decrement player 1's loss count
                records[player2_name]["wins"] += 1
                records[player1_name]["losses"] += 1
              else:
                # Neither player won, so do nothing.
                #records[player2_name]["wins"] += 0
                #records[player1_name]["losses"] += 0
                pass

    sorted_records = None
    # sort records by wins and losses and into slightly different dict layout then sort again by losses
    # using pandas would look cleaner but replit doesn't have pandas module.
    sorted_records = sorted(sorted([{"name": k, "wins": v["wins"], "losses": v["losses"]} for k, v in records.items()], key = lambda x:(x["wins"], x["losses"]), reverse = True), key=lambda x:-x["losses"], reverse = True)
    return sorted_records
    
 
    
    
  except Exception as e:
    print(e)

def leaderboard(app, tournament, participants, matches, FullHostName):
  try:

    records = leaderboard_records(tournament, participants, matches)
    
	  # format the HTML output using CSS styles
    with app.app_context():
	    new_html = render_template('leaderboard.html', parent_list = records, currenttime=int(time.time()), fullhost=FullHostName)

    return new_html  # return the updated HTML
      
  except Exception as e:
    print(e)
    

def leaderboard_data(app, tournament, participants, matches):
  try:

    records = leaderboard_records(tournament, participants, matches)
    
    # format the HTML output using CSS styles
    with app.app_context():
      new_html = render_template('leaderboard_data.html', parent_list = records)

    return new_html  # return the updated HTML
      
  except Exception as e:
    print(e)
