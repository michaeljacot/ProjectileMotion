# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:07:38 2020
                    
                        Created by Michael Jacot de Boinod



         B00772706
         michael.jacot@dal.ca
         
         
         Header Comment:
             This file (guiSim.py) creates the user interface which allows for
             data to be read into the simulation. This is the file that you run
             to start the program. "Simulation.py" is called when the user clicks
             the "Run" button, this method call occurs at line 348. This file uses
             pythons "tkinter" library to create the user interface. The interface
             should scale appropriately with the size of the clients display.
             
         USING THE GUI:
             To properly use this GUI, either select one of the buttons in the pre-set
             frame to automatically input the proper specifications of the respective
             ball, or input your own parameters into the "value" text boxes and hit 
             "Enter Data" to push the values into memory. The program will only take
             float and integer values as parameters. The data that is sent to the 
             "Simulation.py" file is the data that is stored within the "Current Value"
             labels.
                 
"""

import numpy as np
import tkinter as tk
from Simulation import sim
from vpython import *
from math import cos,sin,pi
import numpy as np

root = tk.Tk() #start of window

canvas = tk.Canvas(root,height = 300,width = 500)
canvas.pack()

###outside frame###
#uses pack format
mainframe = tk.Frame(canvas,bg = 'snow4')
mainframe.place(relwidth = 1,relheight = 1)




title = tk.Label(mainframe, text = "Projectile Motion in 3D", bg = "cornflower blue", font = ('Times',18))
title.pack(side = 'top', fill = 'both' ) #title label




#####center frame where data will be inputted#####
#uses grid format
centerframe = tk.Frame(canvas, bg = 'blue')
centerframe.place(relx = 0 ,rely = 0.20,relwidth = 1,relheight = .62)


#preset frame
presets = tk.Frame(centerframe,bg = 'cyan')
presets.place(relheight = 1,relwidth = 0.371,relx = 0.628)


#initial velocity label
ivelLab = tk.Label(centerframe, text = "Initial Velocity (m/s)", bg = "White")
ivelLab.grid(row = "1",column = "1")

#initial velocity textbox
ivelTxt = tk.Entry(centerframe,bg = "white")
ivelTxt.grid(row = '1',column = '2')



#airspeed Label
airspeedLab = tk.Label(centerframe, text = "AirSpeed (x,y,z) (m/s)", bg = "White")
airspeedLab.grid(row = "2",column = "1")

#xairspeed textbox
xairspeedTxt = tk.Entry(centerframe,bg = "white")
xairspeedTxt.grid(row = '2',column = '2')

#yairspeed textbox
yairspeedTxt = tk.Entry(centerframe,bg = "white")
yairspeedTxt.grid(row = '3',column = '2')

#zairspeed textbox
zairspeedTxt = tk.Entry(centerframe,bg = "white")
zairspeedTxt.grid(row = '4',column = '2')



#airturbulance label
airturbLab = tk.Label(centerframe, text = " Air Turbulance")
airturbLab.grid(row = '5', column = '1')

airturbTxt = tk.Entry(centerframe, bg = 'white')
airturbTxt.grid(row = '5' ,column = '2')



#mass label
massLab = tk.Label(centerframe, text = "Mass (kg)")
massLab.grid(row = '6',column = '1')

massTxt = tk.Entry(centerframe, bg = 'white')
massTxt.grid(row = '6', column = '2')



#airdensity
airdenseLab = tk.Label(centerframe, text = "Air Density (kg/m^3)")
airdenseLab.grid(row = '7',column = '1')

airdensityTxt = tk.Entry(centerframe, bg = 'white')
airdensityTxt.grid(row = '7', column = '2')



#ballsize
sizeLab = tk.Label(centerframe, text = "Raduis (m)")
sizeLab.grid(row = '8',column = '1')

sizeTxt = tk.Entry(centerframe, bg = 'white')
sizeTxt.grid(row = '8', column = '2')


#indicator labels

statLab = tk.Label(centerframe, text = 'Parameter').grid(row = '9',column = '1')
valLab = tk.Label(centerframe,text = 'Value').grid(row = '9',column = '2')
curValLab = tk.Label(centerframe,text = 'Curent Value').grid(row= '9',column = '4')
presetLab = tk.Label(presets,text = 'Presets').place(rely = 0.9,relwidth = 1)



######################preset frame buttons##############################

#loads the values for a standard baseball
def loadBaseball():
    
    velocity = 100.0 #m/s
    size = 0.0375 #m
    xas = 0 #m/s
    yas = 0 #m/s
    zas = 0 #m/s
    turb = 1
    mass = .145 #kg
    airDensity = 1.225 #kg/m^3
    
    curVelLab['text'] = velocity
    
    curXASLab['text'] = xas
    
    curYASLab['text'] = yas
    
    curZASLab['text'] = zas
    
    curATLab['text'] = turb
    
    curMassLab['text'] = mass
    
    curADLab['text'] = airDensity
    
    curSizeLab['text'] = size
 
#places the button on the GUI
baseballballButton = tk.Button(presets, text = "Baseball",command = loadBaseball) 
baseballballButton.place(relx = 0.1,rely = 0.1, relheight = 0.3,relwidth = 0.3)



#loads the values for a standard baseball
def loadBasketBall():
    
    velocity = 100.0 #m/s
    size = 0.1213 #m
    xas = 0 #m/s
    yas = 0 #m/s
    zas = 0 #m/s
    turb = 1
    mass = .500 #kg
    airDensity = 1.225 #kg/m^3
    
    curVelLab['text'] = velocity
    
    curXASLab['text'] = xas
    
    curYASLab['text'] = yas
    
    curZASLab['text'] = zas
    
    curATLab['text'] = turb
    
    curMassLab['text'] = mass
    
    curADLab['text'] = airDensity
    
    curSizeLab['text'] = size

#places the button on the GUI
basketballButton = tk.Button(presets, text = "BasketBall",command = loadBasketBall) 
basketballButton.place(relx = 0.6,rely = 0.1, relheight = 0.3,relwidth = 0.3)


def loadBowlingBall():
    
    velocity = 100.0 #m/s
    size = 0.12 #m
    xas = 0 #m/s
    yas = 0 #m/s
    zas = 0 #m/s
    turb = 1
    mass = 8 #kg
    airDensity = 1.225 #kg/m^3
    
    curVelLab['text'] = velocity
    
    curXASLab['text'] = xas
    
    curYASLab['text'] = yas
    
    curZASLab['text'] = zas
    
    curATLab['text'] = turb
    
    curMassLab['text'] = mass
    
    curADLab['text'] = airDensity
    
    curSizeLab['text'] = size

#places the button on the GUI
BowlingBallButton = tk.Button(presets, text = "Bowling \nBall",command = loadBowlingBall,wraplength = 500) 
BowlingBallButton.place(relx = 0.1,rely = 0.5, relheight = 0.3,relwidth = 0.3)



def loadSquashBall():
    
    velocity = 100.0 #m/s
    size = 0.020 #m
    xas = 0 #m/s
    yas = 0 #m/s
    zas = 0 #m/s
    turb = 1
    mass = 0.024 #kg
    airDensity = 1.225 #kg/m^3
    
    curVelLab['text'] = velocity
    
    curXASLab['text'] = xas
    
    curYASLab['text'] = yas
    
    curZASLab['text'] = zas
    
    curATLab['text'] = turb
    
    curMassLab['text'] = mass
    
    curADLab['text'] = airDensity
    
    curSizeLab['text'] = size

#places the button on the GUI
SquashBallButton = tk.Button(presets, text = "Squash \nBall",command = loadSquashBall,wraplength = 500) 
SquashBallButton.place(relx = 0.6,rely = 0.5, relheight = 0.3,relwidth = 0.3)




######################end of preset frame buttons##############################


#create all of the display labels
curVelLab = tk.Label(centerframe)
curVelLab.grid(row = '1',column = '3',columnspan = '2')
    
curXASLab = tk.Label(centerframe)
curXASLab.grid(row = '2',column = '3',columnspan = '2')
    
curYASLab = tk.Label(centerframe)
curYASLab.grid(row = '3',column = '3',columnspan = '2')

curZASLab = tk.Label(centerframe)
curZASLab.grid(row = '4',column = '3',columnspan = '2')
    
curATLab = tk.Label(centerframe)
curATLab.grid(row = '5',column = '3',columnspan = '2')
    
curMassLab = tk.Label(centerframe)
curMassLab.grid(row = '6',column = '3',columnspan = '2')

curADLab = tk.Label(centerframe)
curADLab.grid(row = '7',column = '3',columnspan = '2')
    
curSizeLab = tk.Label(centerframe)
curSizeLab.grid(row = '8',column = '3',columnspan = '2')
    

#gets the info loaded into the labels and returns the values
def getInfo():
    
    curVel = curVelLab['text'] 
    
    
    curXAS = curXASLab['text']
    
    
    curYAS = curYASLab['text']
     
    
    curZAS = curZASLab['text']
     
    
    curAT = curATLab['text'] 
   
    
    curMass = curMassLab['text']
    
    
    curAD = curADLab['text']
     
    
    curSize = curSizeLab['text']
    
    
    #returns the values to be used in calculation
    return curVel,curXAS,curYAS,curZAS,curAT,curMass,curAD,curSize


def clear():

    curVelLab['text'] = ""
    
    curXASLab['text'] = ""
    
    curYASLab['text'] = ""
    
    curZASLab['text'] = ""
    
    curATLab['text'] = ""
    
    curMassLab['text'] = ""
    
    curADLab['text'] = ""
    
    curSizeLab['text'] = ""
    
    
#wrpper method for running the simulation
def runSim():
    
    #have to cast the output of this to float and list to convert into a form that sim will take as args
    inputs = list(getInfo())
    inputs = [float(i) for i in inputs]
    
    sim(inputs[0],inputs[1],inputs[2],inputs[3],inputs[4],inputs[5],inputs[6],inputs[7])

def enterData():
    
    
    curVel = ivelTxt.get()
    if curVel != "" : curVelLab['text'] = curVel
    
    curXAS = xairspeedTxt.get()
    if curXAS != "" : curXASLab['text'] = curXAS
    
    curYAS = yairspeedTxt.get()
    if curYAS != "" : curYASLab['text'] = curYAS
    
    curZAS = zairspeedTxt.get()
    if curZAS != "" : curZASLab['text'] = curZAS
    
    curAT = airturbTxt.get()
    if curAT != "" : curATLab['text'] = curAT
    
    curMass = massTxt.get()
    if curMass != "" : curMassLab['text'] = curMass
    
    curAD = airdensityTxt.get()
    if curAD != "" : curADLab['text'] = curAD
    
    curSize = sizeTxt.get()
    if curSize != "" : curSizeLab['text'] = curSize
    


#bottom buttons
enterdata = tk.Button(mainframe, text = "Enter data",command = enterData) 
enterdata.pack(side = 'left',anchor = 's') #enter data button

cleardata = tk.Button(mainframe,text = "Clear data",command = clear)
cleardata.pack(side = 'right',anchor = 's')

runSim = tk.Button(mainframe,text = "Run",command = runSim)
runSim.pack(side = 'bottom',anchor = 's')


root.mainloop() #end of window

