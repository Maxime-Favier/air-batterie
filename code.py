# python: play sound from arduino serial
# Use python 3.6.1 or greater
#
# -*- coding: latin-1 -*-
#
# required pyserial : https://sourceforge.net/projects/pyserial/files/pyserial/
#
# installation:
# cd python-dir/Scripts
# pip.exe install pyserial
#
#
# lunch with cmd
# cd your_script_folder
# name_of_the_script.py
# Ctrl + C to stop script
#
# code created by Maxime_le_Goupil support : maxime1.favier@free.fr
# GNU attribution
# Coded for the "air batterie" project
# Doesnt work on rpi

import sys            # library for system functions (included in python default installation)
import time           # library for delay functions (included in python default installation)
import serial         # library for connecting to the Arduino
import winsound       # library for playing sound (included in python default installation)
import ctypes         # librarys for messages boxes (included in python default installation)
from tkinter import *



def Mbox(title, text, style):   # fonction for Mbox
    ctypes.windll.user32.MessageBoxW(0, text, title, style)

# default port for the arduino for my system - update to match your system
default_arduino_port = "COM6"

def main(arduino = default_arduino_port):      
    print ("Connecting to Arduino on port ", arduino)
    try:
        ser = serial.Serial(arduino, timeout=1)                 # connect to the Arduino
        Mbox('Connection to arduino', 'Successfully connected to Arduino ', 0)
        print ("Successfully connected to Arduino on ", arduino)
        arduino_opened = 1
    except:
        Mbox('Connection to arduino', 'Failed to connect Arduino Stopping ...', 0)
        print ("Failed to connect Arduino on port ", arduino)
        arduino_opened = 0


 # if the Arduino was successfully connected, start reading and processing tags    
    if arduino_opened:
        while 1:    # loop forever until a "quit" tag is read

            data=str(ser.readline())    #read data from serial
            print(data)
            data = data[7]		#read the 7th character of the str
            # Uncomment for debug
            #Mbox('DEBUG', data, 0)
            
            #SOUND A
            if data == 'a':  #Sound A --> sounda in serial monitor Serial.println("sounda");
                
                try:
                    winsound.PlaySound('#HERE YOUR SOUND DIRECTORY', winsound.SND_FILENAME)    #USE .WAV
                    #USE DOUBLE SLASH ex: C:\\Users\\Adhérent\\Downloads\\surroundTestDTS.dts.wav
                    print ("sound play A")
                    
                except:
                    Mbox('Sound play', 'failled to play sound A Stopping ...', 0)
                    print ("failled to play sound A")
            
            #SOUND B
            if data == 'b':  #Sound B --> sounda in serial monitor Serial.println("soundb");
                
                try:
                    winsound.PlaySound('#HERE YOUR SOUND DIRECTORY', winsound.SND_FILENAME)    #USE .WAV
                    #USE DOUBLE SLASH ex: C:\\Users\\Adhérent\\Downloads\\surroundTestDTS.dts.wav
                    print ("sound play B")
                    
                except:
                    Mbox('Sound play', 'failled to play sound B Stopping ...', 0)
                    print ("failled to play sound B")
            
            #SOUND C
            if data == 'c':  #Sound C --> soundc in serial monitor Serial.println("soundc");
                
                try:
                    winsound.PlaySound('#HERE YOUR SOUND DIRECTORY', winsound.SND_FILENAME)    #USE .WAV
                    #USE DOUBLE SLASH ex: C:\\Users\\Adhérent\\Downloads\\surroundTestDTS.dts.wav
                    print ("sound play C")
                    
                except:
                    Mbox('Sound play', 'failled to play sound C Stopping ...', 0)
                    print ("failled to play sound C")
            
            #SOUND D
            if data == 'd':  #Sound D --> sounda in serial monitor Serial.println("soundd");
                
                try:
                    winsound.PlaySound('#HERE YOUR SOUND DIRECTORY', winsound.SND_FILENAME)    #USE .WAV
                    #USE DOUBLE SLASH ex: C:\\Users\\Adhérent\\Downloads\\surroundTestDTS.dts.wav
                    print ("sound play D")
                    
                except:
                    Mbox('Sound play', 'failled to play sound D Stopping ...', 0)
                    print ("failled to play sound D")
             
            time.sleep(0.5)     #delay for pyserial reading just in case

main()      #starter
