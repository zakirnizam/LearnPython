import pyttsx3 #Imported TEXT to SPEECH Module
engine = pyttsx3.init()

engine.say("Dear Nizam , I have reserved your veg meal for a day, " \
"Have a Nice day")
engine.runAndWait()
engine.stop()