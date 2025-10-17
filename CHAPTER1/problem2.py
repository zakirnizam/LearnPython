import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 
engine.say("Dear Nizam , I have reserved your veg meal for a day, Have a Nice day!!!")
engine.runAndWait()
engine.stop()