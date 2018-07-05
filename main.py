import os
import sys

import speech_recognition as sr
# from time import ctime
import time
from gtts import gTTS

from opts import parse_opts

from jarvis import jarvis, news_update, check_battery, take_rest, speak, recordAudio
from pickle import pickle

if __name__ == '__main__':
  opt = parse_opts()
  print(opt)

  # initialization
  time.sleep(2)
  pickle(opt)
  speak("Hi {}, welcome to dimension 214!".format(opt.user))
  while True:
    try:
      print("********************************")
      print("Press Ctrl + C to provide input")
      print("********************************")
      while True:
        sec = int(time.strftime("%S",time.localtime(time.time())))
        if (sec == 0 ):
          minutes = int(time.strftime("%M",time.localtime(time.time())))
          if (minutes % 10 ==0):
            # check battery not just battery level
            print("..Checking battery")
            check_battery()
          if (minutes % 60 == 0):
            # news update should be queued
            print("..Getting news update")
            news_update(opt)
          if (minutes % 15 == 0):
            take_rest()
    except KeyboardInterrupt:
      if opt.audio:
        data = recordAudio()
      else:
        data = raw_input('\n>> ')
      jarvis(opt, data)

