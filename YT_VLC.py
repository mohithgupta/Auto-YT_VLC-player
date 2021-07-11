import clipboard
import threading 
import time
import os
import sys
from win10toast import ToastNotifier
from win32gui import GetWindowText, GetForegroundWindow
def done(systray):

    sys.exit()

def about(systray):

    command_about="start https://github.com/mohithgupta"

    os.system(command_about)

def run_step2():
    
    link=clipboard.paste()
    
    if( ( link.find("https://www.youtube.com/watch?v=")==0 or link.find("https://www.youtube.com/playlist?list=")==0 ) and "-vlc" in link):
        link=link[:-4]
        command = ("vlc " + clipboard.paste())  # text will have the content of clipboard
        os.system('cd /d C:\\Program Files\\VideoLAN\\VLC')
        os.system(command)
        clipboard.copy('')
    
    else:
    
        pass

def get_active():

    while True:

        time.sleep(0.5)

        if(GetWindowText(GetForegroundWindow())[-6:]=="Chrome" or GetWindowText(GetForegroundWindow())[-4:]=="Edge"):
            run_step2()

if __name__ == "__main__": 
   
    from pathlib import Path
    from infi.systray import SysTrayIcon
    toaster = ToastNotifier()
    toaster.show_toast("YLC","I am running in Background ✔️",icon_path=str(Path(__file__).parent.absolute())+"\\icon\\vlc_yt.ico",duration=3,threaded=True)
    menu_options = (("About", None, about),)
    systray = SysTrayIcon(str(Path(__file__).parent.absolute())+"\\icon\\vlc_yt.ico", "YT_VLC", menu_options,on_quit=done)
    systray.start()
    t1 = threading.Thread(target=get_active) 
    t1.start()