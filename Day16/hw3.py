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


def vowelCount(sentence):
  sentence = sentence.lower()

  count_a = sentence.count("a")
  count_e = sentence.count("e")
  count_i = sentence.count("i")
  count_o = sentence.count("o")
  count_u = sentence.count("u")

  print(
      f"a, e, i, o, and u appear, respectively, {count_a}, {count_e}, {count_i}, {count_o}, {count_u} times."
  )


def crypto(filename):
  file = open(filename, "r")
  content = file.read()
  modified_content = content.replace("secret", "xxxxxx")
  print(f"{modified_content}\n")


def links(filename):
  file = open(filename, "r")
  content = file.read()
  number_of_a_tag = content.count("</a>")
  return number_of_a_tag


def duplicate(filename):
  file = open(filename, "r")
  content = file.read()

  for punctuation in ".,?":
    content = content.replace(punctuation, "")

  content = content.lower()

  content = content.split(" ")

  # print(content)

  duplicated_words = []
  
  for word in content:
    if word in duplicated_words:
      return True
    duplicated_words.append(word)

  return False
    


if __name__ == "__main__":
  import doctest
  print(doctest.testfile("hw3TEST.py"))


