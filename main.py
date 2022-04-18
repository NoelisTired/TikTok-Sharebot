import os
try:
    import requests
    import pystyle
    from pystyle import Colors, Colorate, Add, Center, Box, Write
    import threading
    from threading import Thread
except:
    os.system("pip install requests")
    os.system("pip install threading")
    os.system("pip install pystyle")
import requests
import pystyle
from pystyle import Colors, Colorate, Add, Center, Box, Write
import threading
from threading import Thread

print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"[NoelP X] Welcome to the (open-source) client to interact with a lil project that has been worked on"), 1))
print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"As of right now there's a ratelimit of 10.000 shares/day\n\n"), 1))
videoid = Write.Input(Center.XCenter("Enter your Video/VideoID > "), Colors.red_to_white, interval=0.0100)
try:
    int(videoid)
except:
    r = requests.get(videoid)
    if "vm" or "://m." in videoid:
        try:
            videoid = r.url.split("video/")[1].split("?")[0]
        except:
            try:
                videoid = r.url.split("https://m.tiktok.com/v/")[1].split(".html")[0]
            except:
                print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter("Please enter a valid URL!"), 1))
    elif "https://www.tiktok.com/@" in videoid:
        videoid = videoid.split("https://www.tiktok.com/@")[1].split("/")[0]
    else:
        print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter("Please enter a valid URL!"), 1))

key = Write.Input(Center.XCenter("Enter your key: (noelp.live) "), Colors.red_to_white, interval=0.0100)
while True:
    response = requests.get(f"https://noelp-backend.xyz/shares?id={str(videoid)}&key={key}")
    if response.status_code == 200:
        print(response.text)
    elif response.status_code == 429:
        print("Exceeded ratelimit, come back in 24 hours!")
