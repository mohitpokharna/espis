import os

def play_playlist(album):
  if "hindi" in album:
    os.system("google-chrome https://www.youtube.com/watch?v=7Zqk0YZAawI&list=PL9BCachlIkC_plFo3uOqVYIKSS8kXuyMy")
  else:
    os.system("google-chrome https://www.youtube.com/watch?v=6h2h4zIhwuM&list=PL9BCachlIkC_l2p5fI-marPgdZ_ungkHq")


def play_random():
  os.system("google-chrome https://www.youtube.com/watch?v=kV-2Q8QtCY4&list=PL9BCachlIkC_l2p5fI-marPgdZ_ungkHq&index=16")


