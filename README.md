# something-awesome
## Ass.py

A quiet keylogger for Windows, which:
  * hides terminal winow
  * Logs key-presses
  * Logs window title of window-in-focus for each key
  
download the appropriate PyHook and PyWin32 .whl file that correspond to your windows version and python version that you are running
https://www.lfd.uci.edu/~gohlke/pythonlibs/

use this stack overflow thread to help you to install the packages
https://stackoverflow.com/questions/27885397/how-do-i-install-a-python-package-with-a-whl-file

*pip install and run program from windows powershell*

To kill/stop the program end the python program that is running in task manager

usage: `python3 ass.py`

## osx-keylogger.py

A quiet keylogger for osx(tested)/*nix(untested). Compared to above, only captures keypressses. 

installation: `pip3 install -r requirements.txt`

usage: `nohup python3 osx-keylogger.py &` 
  * Will place the program in the background so it runs silently, persisting even through closing of session. 
  
output is saved to `~/.not_a_keylogger.txt`


Idea derived from [here](https://github.com/HusseinBakri/Tanit-Keylogger) and the Tanit-Keylogger by Hussein Bakri
