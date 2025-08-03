# print("Hello! I am learning Python!");



# # 1. Write a program to print Twinkle twinkle little star poem in python. 

# print("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.")



# import pyjokes
# print(pyjokes.get_joke())


"""directory = "."
import os
list = os.listdir(directory)
print("Files in directory:", list)"""

import pyttsx3
engine = pyttsx3.init()

engine.say("Hello! My name is Ramzan Shaikh! and i am learning Python.")
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        # printing current voice rate
engine.setProperty('rate', 250)
engine.runAndWait()