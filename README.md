## How To use :-

- Clone this repo and extract files to your desired location.

- Run YT_VLC.exe (Or you can also run the source code script in your editor)

- If everything runs good, a Notification will show up with "I am Running in Background" text

- You just need to add "-play-in-vlc" to your YouTube URL and copy it and you are done ✔️ 

- It automatically opens VLC and plays your video.

- To close the application, go to system tray icon --> right click the vlc icon (the vlc icon may not show up due to some errors but atleast default script icon will be showed) --> click on "quit"


## How It Works :-

- The scripts looks for the clipboard actions.

- After checking certain **conditons** such as : 

    - Current active window? - active window can be chrome or microsoft edge
    - Incorrect URL? - should be a youtube video 
    - Youtube Streamable Link ? - should be a youtube video
    - Explicit input of `-play-in-vlc`? - link should have "-play-in-vlc" at the end

- Script then executes a command line tool provided by VLC which allows VLC to stream videos. It auto copy-pastes with required commands and plays the video.
 

# Actual Process :-

- Go to YouTube  --> copy video url --> open VLC --> open network streamable file --> paste url --> then watch video

( Why do all this, when you can have a complete automated script that does most of you manual work with just a couple of keystrokes 👌 )

# Simplified to :- (with just few lines of code and hours of research ofcourse....)

- Go to YouTube --> add "-play-in-vlc" to URL and copy it --> run the YT_VLC.exe file (or you can first run the exe, then copy url)

- That's it!!! you can watch it already...


## Other Info

- The code file is named as "YT_VLC.py" changes can be made there.

- It is open source you can clone and change code to your need.

- For any clarification on code or any errors you face, you can contact me any time. Mail me at mohithguptak@gmail.com - I'll reach you back in short.

- Currently Supports only **Windows 10 64Bit**


Used Libraries :-

[Clipboard]: <https://pypi.org/project/clipboard/>

[Win10toast]: <https:/github.comjithurjacobWindows-10-Toast-Notifications>

[Win32gui]:<https://pypi.org/project/win32gui/>

[infi.systray]: <https://github.com/Infinidat/infi.systray>

