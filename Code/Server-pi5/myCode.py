#Import everything in the control module, 
#including functions, classes, variables, and more.

from Control import *

#Creating object 'control' of 'Control' class.
control=Control()

#Using the forWard function, let the robot dog move forward five steps and keep standing.
for i in range(5):
	control.forWard()
control.stop()

#Turn the robot dog's body 10 degrees to the right
for i in range(10):
	control.attitude(0,0,i)
	time.sleep(0.1)

#Turn the robot dog's body 20 degrees to the left	
for i in range(10,-10,-1):
	control.attitude(0,0,i)
	time.sleep(0.1)
	
#Straighten the robot dog's body
for i in range(-10,0,1):
	control.attitude(0,0,i)
	time.sleep(0.1)	

#Using the forWard function, let the robot dog move forward five steps and keep standing.
for i in range(5):
	control.forWard()
control.stop()