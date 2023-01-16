
def player_name(participants, id):
  for parti in participants:
    if parti['id'] == id:
      return parti['name']

  return "Unknown"