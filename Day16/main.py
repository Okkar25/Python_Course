def cheer(team_name):
  print("How do you spell winner?")
  print("I know, I know!")

  # spaced_team = " ".join(team_name.upper())
  # print(f"{spaced_team} !")
  
  spaced_name = ""
  for char in team_name.upper():
    spaced_name += char + " "
  print(f"{spaced_name}!")
  

  print("And that's how you spell winner!")
  print(f"Go {team_name}!")


