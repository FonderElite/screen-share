from vidstream import ScreenShareClient
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
print(wi  + gr  + 'Client for connecting to the server.')
ip = input(wi + yl + 'IP: ')
try:
    s.inet_aton(ip)
    print(wi + 'Checking if IP  is Valid...')
    time.sleep(1.5)
    print(wi + gr + 'IP is Valid!')
except socket.error:
    print(Fore.RED + 'IP is not Valid.')
port = input(wi + yl + 'Port: ')  
choice = ['0=Camera','1=Video','2=ScreenShare']
print(choice[0],choice[1],choice[2])
client = input(wi + gr + os + "-User: ")
client1 = CameraClient(ip, 9999)
client2 = VideoClient('192.168.1.100', 9999, 'video.mp4')
client3 = ScreenShareClient('192.168.1.100', 9999)
if client == 0:
   client1.start_stream()
   print(wi + gr + 'Starting Camera Client...')
  time.sleep(1.5)
elif client == 1:
   print(wi + gr + 'Starting Video Client...')
   time.sleep(1.5)
  client2.start_stream()
elif client == 2:
   print(wi + gr + 'Starting Screen-Sharing Client...')
   time.sleep(1.5)
  client3.start_stream()
else:
  print(wi + rd + 'Please Specify.')
