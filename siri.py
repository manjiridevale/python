import pyttsx3
import os

# pyttsx3.speak("hello its siri how can i help you")
while True:
	print("Whats on Your Mind  : " , end='')
	p = input()

	# print(p)
	# os.system(p)

	if (("run" in p) or ("execute" in p ) or ("open" in p )) and (("chrome" in p) or ("google" in p)):
  		os.system("chrome")
	
	elif (("run" in p) or ("open" in p )) and (("alarm" in p) or ("time" in p)) :
  		os.system("clock")

	elif (("good" in p ) and ("morning" in p)) :
  		print("Good Morning")
	
	elif (("good" in p ) and ("night" in p)) :
  		print("Good Night")
	
	elif (("good" in p ) and ("afternoon" in p)) :
  		print("Good Afternoon")

	elif (("run" in p) or ("execute" in p ) or ("open" in p )) and (("notepad" in p) or ("editor" in p)) :
  		os.system("notepad")

	elif (("open" in p )) and ("camera" in p) :
  		os.system("camera")

	elif (("run" in p) or ("execute" in p ) or ("open" in p )) and (("drawing board" in p) or ("Paint" in p)) :
  		os.system("Paint")

	elif (("open" in p )) and ("map" in p) :
  		os.system("map")
	
	elif (("run" in p) or ("execute" in p )) and ("calculator" in p) :
  		os.system("calculator")
	
	elif (("run" in p) or ("execute" in p )) and ("word" in p) :
  		os.system("word")

	elif ("exit" in p) or ("quit" in p):
		break
	else:
  		print("Invaild input please try again")