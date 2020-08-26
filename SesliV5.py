import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
import os 
from tkinter import *
from pyautogui import *

#--
pencere=Tk()
pencere.title("Sesli Asistan V5")
pencere.geometry("800x500+50+50")
pencere.configure(background="black")

isim=Label(text="What is your name?  ")
isim.config(font="bold 20",fg="cyan",bg="black")
isim.grid(row=1,column=1)

name=Entry()
name.config(font="bold 20",fg="orange",bg="black")
name.grid(row=1,column=2)

komutlar=Label(text="Commands:")
komutlar.config(font="bold 20",fg="blue",bg="black")
komutlar.grid(row=4,column=1)







def a():

  
  r=sr.Recognizer()
  with sr.Microphone() as source:
    label1=Label(text="Asistant is ready: ")
    label1.config(font="bold 20",fg="black",bg="black")
    label1.grid(row=5,column=1)
    audio=r.listen(source)
    label3=Label(text=name.get())
    label3.config(font="bold 20",fg="white",bg="black")
    label3.grid(row=6,column=1)
  try:
    ses=str(r.recognize_google(audio))

    if 'calculator' in ses:
      os.system("calc")
      
    if 'keyboard' in ses:
      os.system("osk")
      
    if 'task manager' in ses:
      os.system("taskmgr")
      
    if 'note' in ses:
      os.system("notepad")

    
    if 'screenshot' in ses:
      seskayıt=gTTS(text="screenshot taking after 5 seconds")
      seskayıt.save("screenshot.waw")
      os.system("screenshot.waw")
      time.sleep(5)
      ss1=screenshot()
      ss1.save(r"screenshot.png")
      os.system("screenshot.png")
      
    if 'hello' in ses:
      seskayıt=gTTS(text="hello")
      seskayıt.save("hello.waw")
      os.system("hello.waw")  

    if 'how are you' in ses:
      seskayıt=gTTS(text="i  am fine and you?")
      seskayıt.save("howareyou.waw")
      os.system("howareyou.waw")
    
 
    if 'shutdown' in ses:
      os.system("shutdown /s")
      seskayıt=gTTS(text="your computer will be shutdown")
      seskayıt.save("shutdown.waw")
      os.system("shutdown.waw")
      
    
    if 'cancel' in ses:
      os.system("shutdown /a")
      seskayıt=gTTS(text="your computer will not shutdown")
      seskayıt.save("shutdowncancel.waw")
      os.system("shutdowncancel.waw")
      
       
    

  except sr.WaitTimeoutError:
    seskayıt=gTTS(text="i can't understand you")
    seskayıt.save("waittime.waw")
    os.system("waittime.waw")

  except sr.UnknownValueError:
    seskayıt=gTTS(text="I can't do anything about this sound")
    seskayıt.save("unknownvalue.waw")
    os.system("unknownvalue.waw")

  



buton=Button()
buton.config(text="Start Asistant",font="Bold 20",fg="aqua",bg="black",command=a)
buton.grid(row=3,column=3)







pencere.mainloop()
