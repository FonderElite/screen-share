from vidstream import ScreenShareClient
from vidstream import CameraClient
from vidstream import VideoClient
from colorama import  Fore
import socket as s
import time
import platform
# Choose One
os = platform.system()
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
banner = print(gr + '''
 ___________
||         ||            _______
|| Client  ||           | _____ |
||         ||           ||_____||
||_________||           |  ___  |
|  + + + +  |           | |___| |
    _|_|_   \           |       |
   (_____)   \          |==   ==|
              \    ___  |       |
       ______  \__/   \_| _____ |
      |   _  |      _/  | |___| |
      |  ( ) |     /    |_______|
      |___|__|    /       Server
           \_____/

''')
print(wi + Fore.CYAN  + 'Client for connecting to the server.')
ip = input(wi + 'IP: ')
try:
    s.inet_aton(ip)
    print(wi + 'Checking if IP  is Valid...')
    time.sleep(1.5)
    print(wi + gr + 'IP is Valid!')
except socket.error:
    print(Fore.RED + 'IP is not Valid.')
port = input(wi + 'Port: ')  
choice = ['0=Camera','1=Video','2=ScreenShare']
print(wi + choice[0],choice[1],choice[2])
client = input(wi + gr + os + "-User: ")
client1 = CameraClient(ip, 9999)
client2 = VideoClient(ip, 9999, 'video.mp4')
client3 = ScreenShareClient(ip, 9999)
if client == '0':
  client1.start_stream()
  print(wi + 'Starting Camera Client...')
  time.sleep(0.5)
  print(wi + gr + 'Camera Client has started.')
elif client == '1':
  client2.start_stream()
  print(wi + 'Starting Video Client...')
  time.sleep(0.5)
  print(wi + gr + 'Video Client has started.')
elif client == '2':
  client3.start_stream()
  print(wi + Fore.CYAN + 'Starting Screen-Sharing Client...')
  time.sleep(0.5)
  print(wi + gr + 'Share Screen Client has started.')
  
else:
  print(rd + 'Please Specify.')
