from flask import render_template
import time
import players

def versus_players(tournament, participants, matches):
  try:
    P1Name = 'Player 1'
    P2Name = 'Player 2'

    # get list of open matches
    for match in matches:
      if match["state"] == "open":
        if match["underway_at"] is not None:
          Player1ID = int(match['player1_id'])
          Player2ID = int(match['player2_id'])
            
          P1Name = players.player_name(participants, Player1ID)
          P2Name = players.player_name(participants, Player2ID)
    return P1Name, P2Name
          
  except Exception as e:
    print(e)

    
def versus(app, tournament, participants, matches):
  try:
    P1Name, P2Name = versus_players(tournament, participants, matches)
  
    # format the HTML output using CSS styles
    with app.app_context():
      new_html = render_template('versus.html', P1Name=P1Name, P2Name=P2Name, currenttime=int(time.time()))
      return new_html  # return the updated HTML
  except Exception as e:
    print(e)

def versus_data(app, tournament, participants, matches):
  try:
    P1Name, P2Name = versus_players(tournament, participants, matches)
    
    # format the HTML output using CSS styles
    print("rendering vs data")
    with app.app_context():
      new_html = render_template('versus_data.html', P1Name=P1Name, P2Name=P2Name, currenttime=int(time.time()))
      return new_html  # return the updated HTML
  except Exception as e:
    print(e)



    