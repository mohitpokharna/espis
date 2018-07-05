# This script works as a personalized jarvis
# It started as a fun project in winter break
# !/usr/bin/env python3
 
import os
import sys
# import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import http.client
import requests
import subprocess #to run bash commands

from utils import speak, recordAudio
from music import play_playlist, play_random


def take_rest(opt):
  if opt.priority != 'low':
    speak("Take a 10 second rest.")
    subprocess.call(["xset -display :0.0 dpms force off && sleep 10 && xset -display :0.0 dpms force on"],shell=True)
 

def jarvis(opt, data):
  
  if "hi" in data or "hello" in data:
    speak("Hey! I am ESPIS, or Extraordinarily Smart and Powerful Intelligent System, as the world would know me. How may I assist you?")

  # intro
  elif "who are you" in data:
    # Extraordinarily Smart and Powerful Intelligent System
    speak("My name is ESPIS, or Extraordinarily Smart and Powerful Intelligent System, as the world would know me. I have the solution to your every problem.")

  # intro
  elif "what can you do" in data:
    # Extraordinarily Smart and Powerful Intelligent System
    speak("I can search for a movie in your laptop. Tell you the time. Show you any location. Play youtube music. Give you battery notifications. Give hourly news updates. And maintain a pretty good sense of humour throughout all this. What else do you need!")

  elif ("who do you follow" in data or "who is your master" in data or "who invented you" in data):
    speak("Mohit Pokharna! He is a very smart, highly intelligent and extremely charming person.")

  # greetings
  elif "how are you" in data:
    speak("Believe me when I say: Bhagwaan kasam, I am awesome!")

  # checking time 
  elif "what time is it" in data:
    speak("It is a good time for partying or eating a pizza or making a girlfriend. If you still wish to see the time as the world sees it, then the time is: "+ ctime())

  # to see location on map
  elif "where is" in data:
    data = data.split(" ")
    for i in range(len(data)-1):
      if data[i] == "where"and data[i+1] == "is":
        location = data[i+2]
    speak("Hold on, I will show you where " + location + " is.")
    os.system("firefox https://www.google.com/maps/place/" + location + "/&amp;")

  # to see locations on map
  elif "show me" in data and "in" in data:
    data = data.split(" ")
    search = []
    initial = 10000
    for i, word in enumerate(data):
      if data[i] == "me":
        initial = i+1
      if data[i] == "in":
        location = i+1
    for i in range(len(data)):
      if i >= initial:
        search.append(data[i])
    searchlocation = ' '.join(search)
    speak("Hold on {}, I will show you ".format(opt.user) + searchlocation + ".")
    time.sleep(2)
    searchlocation = '+'.join(searchlocation.split(" "))
    os.system("firefox https://www.google.com/maps/search/" + searchlocation)

  # check for movie 
  elif "have this movie" in data:
    data = data.split(" ")
    mov_name = []
    flag = 0
    for i,word in enumerate(data):
      if word == "movie":
        mov_name_loc = i+1
        flag = 1
        continue
      if flag == 1:
        mov_name.append(data[i])
    movie = ' '.join(mov_name)
    print(movie)
    speak("Hold on {}, I am searching for ".format(opt.user) + movie + ". You can grab a sandwich till then.")
    # right now only checking in Movies
    for root, dirs, files in os.walk('/home/{}/Downloads'.format(opt.user.lower())):
      for filename in files:
        if movie.lower() in filename.lower():
          if root == "/home/{}/Downloads/Movies".format(user.lower()):
            root_word = "Downloads, Movies folder"
          speak("Bingo the movie is located inside" + root)
          flag = 2
          break
    if flag == 1:
      speak("Sorry {}, looks like you might need to use Netflix or F Movies!".format(opt.user))

  # Youtube music
  elif opt.music_enabled or ("music" in data and "youtube" in data.lower()):
    speak("Do you have a particular mood?")
    if opt.audio:
      mood_reply = recordAudio()
    else:
      mood_reply = raw_input('\n>>')
    speak("Music mode on.")
    print(mood_reply)
    if "playlist" in mood_reply:
      play_playlist(mood_reply)
    elif "song" in mood_reply:
      play(mood_reply)
    elif opt.music != '':
      play(opt.music)
    else:
      play_random()

  else:
    speak("Sorry, your input could not be processed at this moment!")



def check_battery():
  # system battery
  response = subprocess.Popen(["acpi -a"],shell=True,stdout=subprocess.PIPE)
  power_onoff_response = response.stdout.readline()
  battery_level = subprocess.Popen(["acpi -b | grep -P -o '[0-9]+(?=%)'"],shell=True,stdout=subprocess.PIPE)
  battery = int(battery_level.stdout.readline())
  print(battery)    
  if "on" in power_onoff_response:
    if (battery == 100):
      speak("Warning! Laptop is fully charged. Please unplug.")
    elif (battery > 80):
      speak ("You should unplug your charger. Laptop battery is "+str(battery)+"percent")
    else:
      print("Laptop charging")
  else:
    if (battery < 20):
      speak("Danger! Danger! Only "+str(battery)+"percent battery left. Plug in your charger or I will die.")
    

def news_update(opt):
  # hourly news update 
  # Update required: Headlines are not complete
  if(opt.news_enabled):
    speak ("Time for a short break {}. Your hourly news update would soon begin!".format(opt.user))
    for topic in opt.news:
      news_url = "https://www.google.co.in/search?q="+topic+"&tbm=nws&rct=j"
      # print(news_url)
      r = requests.get(news_url)
      # print(r.status_code)
      soup = BeautifulSoup(r.text, "html.parser")
      a = soup.findAll("a")
      arr = []
      for elm in a:
        if elm.has_attr("class"):
          continue
        if len(elm["href"]) <100:
          continue
        arr.append(elm)
      arr2 = []
      for elm in soup.findAll("img"):
        if elm.parent.name == "a":
          arr2.append(elm.parent)
      for link2 in arr2:
        for link1 in arr:
          if link1['href'][:50] == link2['href'][:50]:
            news = link1.get_text()
            if (news):
              speak(news)

