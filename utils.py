import speech_recognition as sr
import os
from gtts import gTTS
from requests.exceptions import ConnectionError


def speak(audioString):
  while True:
    try:
      print(audioString)
      tts = gTTS(text=audioString, lang='en')
      tts.save("audio.mp3")
      os.system("mpg321 audio.mp3")
      break
    except ConnectionError:
      continue


def recordAudio():
  # Record Audio
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

  # Speech recognition using Google Speech Recognition
  data = ""
  try:
    # Uses the default API key
    # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    data = r.recognize_google(audio)
    print(("You said: " + data))
  except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
  except sr.RequestError as e:
    print(("Could not request results from Google Speech Recognition service; {0}".format(e)))

  return data

