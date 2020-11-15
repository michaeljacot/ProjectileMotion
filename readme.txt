Michael Jacot de Boinod


**********                           **********
**********Please Read This Before Use**********
**********                           **********




					Graphical 3D Projectile Motion Simulation 




----BEFORE RUNNING THE PROGRAM----

This program uses both tkinter and vpython, you must install both these packages before running the program

run 
"pip install vpython"
and
"pip install tkinter"

in your python shell to install these packages

---------------------------------


Outline: 

	This is a text document outlining the basic function and usage of this program. The project 
attempts to simulate motion of a projectile in three dimensions by solving a set of coupled ODE's
with user inputted data. The output of the calculation is plotted on a three dimensional plane
using the graphical package vpython. The python library tkinter is also used to create the GUI in which
the initial parameters are set. There are three main "classes" in this program. I put the quotes around 
"classes" because I don’t actually use any of the syntax to create actual class structures, I instead 
have methods inside each python file that call each other. 

The file guiSim.py is the main class (the one you run have to run first) 

	The GUI will open and input parameters can be modified. There are four pre-set buttons that allow for 
the standard parameters of each of the specific type of ball to be inputted. 

	When the simulation starts up, you may need to adjust the camera angle. You can do this by holding right click
and dragging with your mouse. You can also zoom by using your scroll wheel.

***Parameters***

Initial Velocity (m/s): 
	The initial velocity of the projectiles at the start of the simulation. The projectiles will all
be launched from an angle of +4 degrees from the x axis.

Air Speed (x,y,z) (m/s):
	The Air Speed parameter allows for a "wind" to be applied to the simulation. The air speed will apply
a constant force to the projectiles which is applied at each tick. There are a set of axis arrows within the vpython
window on start-up. The arrows point in the positive direction for each axis. 
Red - x axis. Green - y axis. Blue - z axis.


Air Turbulence (scalar):
	This is a scalar quantity that allows the implementation of air turbulence. Please read the section on stability
issues before adjusting this parameter.

Mass (kg):
	The mass of each projectile, in kg. Affects drag and the force of gravity.

Air Density (kg/m^3):
	The air density during the simulation. Affects drag.

Radius (m):
	Radius of the projectile. Affects drag.

****************



(NOTE: Running any of these pre-sets with 0 m/s initial velocity allows you to see the terminal velocity 
of each ball. The program outputs the speed of the ball at the end of each round of firing, which lets you 
easily read the terminal velocity.
*only baseball and basketball actually reach their terminal velocity within the allowed range*
The program correctly simulates the terminal velocity to within +-1m/s) 





KNOWN STABILITY ISSUES:

	The program simulates air turbulence by applying small stochastic forces at every tick. This was an easy
way to distinguish individual flight paths for each projectile. This type of air turbulence, while cheap, does result in
stability issues at high values. 

It is NOT recommended that the air turbulence parameter exceed 5, especially for low mass projectiles.


High air speed can also result in stability issues.

