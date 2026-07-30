import soccerdata as sd

fbref = sd.FBref(leagues = "ENG-Premier League", seasons = 2015)


events = fbref.read_events(match_id = "3d8961eb")
events.head()