# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:41:28 2020

                        Created by Michael Jacot de Boinod



        B00772706
        michael.jacot@dal.ca
         
         
        Header Comment: 
             
             This is "Simulation.py". It is called by "guiSim.py" when the "Run" button is pressed.
             There are only two methods in this file, the sim() method and the drag() method. The sim()
             method is the one that is called from "guiSim.py", which takes the parameters inputted from 
             the user in the GUI. 
             
             The basic algorithm within this program is as follows.
             
             1. Generate the scene in browser 
             2. Generate the axis pointers, wall, and floor objects within the scene. 
             3. Generate all of the projectile objects with the initial conditions 
                specified parameters by user inputted parameters and place them within the "pList" list.
             4. Update the positions of the projectiles within a loop using equations of motion derived 
                the ordinary differential equations that dictate projectile motion. The drag() method is 
                called within this loop which applies quadratic drag to the simulation.
             5. Output the final conditions of the projectiles into console.
"""



from vpython import *
import random as ran
import numpy as np

#variable that controls which color the projectiles appear as
c = 0


#equation for quadratic drag
def drag(curAD,area,velocity):
    if velocity<0:
        return -(1/4)*curAD*area*velocity**2
    else:
        return (1/4)*curAD*area*velocity**2
    
  

#def sim()
def sim(curVel,curXAS,curYAS,curZAS,curAT,curMass,curAD,curSize):
    
    global c
    
    """
        Axis Notes:
            Red : x
            Green : y
            Blue : z
    """
    
    #warns the user about the potential instability with high air turbulence
    if (curAT>=5):
        print("***********")
        print("***********")
        print("***********")
        print("***WARNING***")
        
        print("High air turbulence will cause stability issues with low-mass projectiles")
    
        print("***********")
        print("***********")
        print("***********")
    
    #generates the axis 
    pointerx = arrow(pos=vector(0,200,200),      axis=vector(100,0,0), shaftwidth=10,color = color.red)
    pointery = arrow(pos=vector(0,200,200),      axis=vector(0,100,0), shaftwidth=10,color = color.green)
    pointerz = arrow(pos=vector(0,200,200),      axis=vector(0,0,100), shaftwidth=10,color = color.blue)
    
    
    
    prange = 200
    
    numBalls = 10
    
    #change size of display
    scene.width = 1000
    scene.height = 1000
    
    scene.camera.pos = vector(-1000,-prange,0)
    
    #target walls and floor
    wall= box(pos=vector(prange,300,0), length=1, height=1000, width=1000)
    floor = box(pos=vector(-300,-prange,0), length=1000, height=1, width=1000)
    wallright= box(pos=vector(prange - 500,300,500), length=1000, height=1000, width=1)
    wallleft= box(pos=vector(prange - 500,300,-500), length=1000, height=1000, width=1)

    
    #make a list to store all of the sphere objects
    pList = []
    
    #calculate the cross sectional area of the sphere 
    #(doing this now so that we dont have do run this line in a loop later on, since the radius can only change with a new call of sim())
    area = (1/4)*np.pi*(curSize*2)**2
    
    for i in range(numBalls):
        
        clr = [color.red,color.green,color.blue,color.orange,color.yellow]
        
        projectile = sphere(pos = vector(0,0,0),
                        radius = curSize,
                        color = clr[c],
                        make_trail = True)
        
        projectile.speed = curVel # Initial speed.
        projectile.angle = (4)*3.141459/180 # Initial angle, from the +x-axis.
        projectile.mass = curMass
        projectile.velocity = vector(projectile.speed*cos(projectile.angle),
                                 projectile.speed*sin(projectile.angle),
                                 0.1)
        pList.append(projectile)
    
    #checks to see that we dont go over the last index of the color list
    #also reset the color counter if we are at the end of the list
    if c!=(len(clr)-1):
        c+=1
    else:
        c=0 #also reset the color counter if we are at the end of the list
    
    #use the follow attribute to follow the last projectile that was shot
    scene.camera.follow(projectile)
    
    
    grav_field = -9.8 #m/s
    
    dt = 0.01
    time = 0
    
    stopped = []
    
    #Main Loop which runs the simulation
  
    while (True):
        
        rate(200)
    
        #this counter checks to see (every time it ticks) if all of the patricles have stopped
        #controlls if the simulation needs to terminate
        
    
        for o in pList:
            
            
            # Calculate the force.
            # grav_force = vector(0,-o.mass*grav_field,0)
            
            #need to call random on every axis to prevent linear allignment
            
            
            #calculates the magnitude of the velocity for air resistance calculations
            
            #speed = np.sqrt(o.velocity.x**2 + o.velocity.y**2+o.velocity.z**2)
            
            #adds the position of each projectile to a list to be checked for stop conditions later
            stopped.append(o.pos)
            
            
            
            #basically the acceleration but we divide by mass when updating the velocity
            fx = curXAS                         -drag(curAD,area,o.velocity.x)            
            fy = curYAS + grav_field*curMass    -drag(curAD,area,o.velocity.y)
            fz = curZAS +                       -drag(curAD,area,o.velocity.z)
            
            #applies the forces from the air turbulence
            fx += ran.uniform(-0.5,0.5)*curAT 
            fy += ran.uniform(-0.5,0.5)*curAT 
            fz += ran.uniform(-0.5,0.5)*curAT 
            
            
        
            #puts the force components into a vector       
            force = vector(fx,fy,fz)
        
            # Update velocity.
            o.velocity = o.velocity + force/o.mass * dt
        
            # Update position.
            o.pos = o.pos + o.velocity * dt
        
            # Update time.
            time = time + dt
            
        #this is a weird line and will take some explaining
        #this checks for the condition that breaks out of this loop and ends the simulation
        #the conditional checks over each of the x and y positions of the particles and breaks if they
        #are either all out of bounds in the x or y axis (z is ignored)
        # checking this way will cause some of the balls to pass the border by a small margin
        if all(i.x >= prange for i in stopped) or all(i.y <= -prange for i in stopped):
            break
        stopped = []   
        
        
        
    #this is a loop that lists the final states of each projectile 
    print("Final Velocity and Position of Each Projectile")
    projNum = 0
    for o in pList:
        
        speed = np.sqrt(o.velocity.x**2 + o.velocity.y**2+o.velocity.z**2)
        print("Object number: ", projNum )
        print("Final speed ", speed, "m/s" )
        print("Final Position (x,y,z) ", o.pos.x, " m," ,o.pos.y," m,", o.pos.z, " m")
        print()
        projNum+=1
        
        
    