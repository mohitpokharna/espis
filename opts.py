import argparse

def parse_opts():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '--user',
    default='Mohit',
    type=str,
    help='Define the username | Jarvis is not faithful to everyone')
  parser.add_argument(
    '--audio',
    action='store_true',
    help='If true, text to speech is enabled.')
  parser.set_defaults(audio=False)
  parser.add_argument(
    '--music_enabled',
    action='store_true',
    help='Enables music')
  parser.set_defaults(music_enabled=False)
  parser.add_argument(
    '--music',
    default='',
    type=str,
    help='Plays music if specified')
  parser.add_argument(
    '--priority',
    default='high',
    type=str,
    help='Decides the priority of jarvis, certain functions would not be called if priority is low (low | high)')
  parser.add_argument(
    '--news_enabled',
    action='store_true',
    help='Gives hourly news updates if enabled.')
  parser.set_defaults(news_enabled=True)
  parser.add_argument(
    '--news',
    default=['Fifa'],
    type=str,
    help='Customize the hourly news (Default is Fifa)')

  args = parser.parse_args()

  return args
