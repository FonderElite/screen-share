import colorama
import os
import sys
import platform
from colorama import Fore
import vidstream
from vidstream import CameraClient
from vidstream import VideoClient
from vidstream import ScreenShareClient
from vidstream import StreamingServer
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
mach = platform.machine()
os = platform.system()
banner = print(wi + gr + '''
    ..=====.. |==|
    ||     || |= |   Screen-Share Using Python!
 _  ||     || |^*| _
|=| o=,===,=o |__||=|
|_|  _______)~`)  |_|
    [=======]  ()       
''')
def server():
  try:
      cmd = input("Would you like to start a server?(y/n)")
      ip = input('Input Your Ip: ')
      print(Fore.CYAN + 'Waiting For Client...')
      server = StreamingServer(ip,9999)
      if cmd == "y":
       server.start_server()
  except ConnectionError:
      print(rd + "Make sure you have an internet connected!")
  else:
      pass
server()



