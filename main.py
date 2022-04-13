import os
try:
    import requests
    import pystyle
    from pystyle import Colors, Colorate, Add, Center, Box, Write
    import threading
    from threading import Thread
except:
    os.system("pip install requests")
    os.system("pip install requests")
    os.system("pip install threading")
import requests
import pystyle
from pystyle import Colors, Colorate, Add, Center, Box, Write
import threading
from threading import Thread

amount = 10 #Multiply this amount by 1000 to get total views

print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"[NoelP X] Welcome to the (open-source) client to interect with a lil project that has been worked on"), 1))
print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"As of right now there's a ratelimit of 10.000 shares/day\n\n"), 1))
videoid = Write.Input(Center.XCenter("Enter your VideoID > "), Colors.red_to_white, interval=0.0100) #If any braindead fuck inputs a full url here i'm not resetting your ratelimit
while True:
    response = requests.get(f"https://noelp-backend.xyz/shares?id={str(videoid)}")
    if response.status_code == 200:
        print("We've sent 1000 Shares!")
        
    elif response.status_code == 429:
        print("Exceeded ratelimit, come back in 24 hours!")
