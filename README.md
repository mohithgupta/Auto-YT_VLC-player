## What it Does ??

### Plays YouTube videos in your VLC with just few clicks

### **Coded in Python**

### Libraries Used 🛠  

- **[Clipboard]**
- **[Win10toast]**
- **[Win32gui]**
- **[infi.systray]**


## How To use :-

- Clone this repo and extract files to your desired location.

- Run YT_VLC.exe (Or you can also run the source code script in your editor)

- If everything runs good, a Notification will show up with `I am Running in Background ✔️` text

- You just need to add "-vlc" to your YouTube URL and copy it and you are done ✔️ 

- Sit back and relax. It automatically opens VLC and plays your video.

- To close the application, go to system tray icon --> Right click the vlc icon (the vlc icon may not show up due to some errors but atleast default script icon will be showed) --> Click on "quit"

(For System Tray - Click the arrow beside your Wifi or Battery Icon)


## How It Works :-

- The scripts looks for the clipboard actions.

- After checking certain **conditons** such as : 

    - Current active window? - active window can be chrome or microsoft edge
    - Incorrect URL? - should be a youtube video 
    - Youtube Streamable Link ? - should be a youtube video
    - Explicit input of `-vlc`? - link should have "-vlc" at the end

- Script then executes a command line tool provided by VLC which allows VLC to stream videos. It auto copy-pastes with required commands and plays the video.
 

## Actual Process :-

- `Go to YouTube  --> Copy video url --> Open VLC --> Open network streamable file --> Paste url --> Then watch video`

( Why do all this, when you can have a complete automated script that does most of you manual work with just a couple of keystrokes 👌 )

## Simplified to :- 

(With just few lines of code and hours of research ofcourse....)

- `Go to YouTube --> Add "-vlc" to URL and copy it --> Run the YT_VLC.exe file` (or you can first run the exe, then copy url)

- That's it!!! you can watch it already...


## Other Info

- The source code file is named as "YT_VLC.py" . Any changes can be made there.

- It is open source you can clone and change code to your need.

- For any clarification on code or any errors, you can contact me any time. Ping me at mohithguptak@gmail.com - I'll reach you back in short.

Received inspiration from [Asish Raju](https://github.com/AsishRaju) and also some help to deal with some errors.

[Clipboard]: <https://pypi.org/project/clipboard/>

[Win10toast]: <https:/github.comjithurjacobWindows-10-Toast-Notifications>

[Win32gui]:<https://pypi.org/project/win32gui/>

[infi.systray]: <https://github.com/Infinidat/infi.systray>

