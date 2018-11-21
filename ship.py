import pyglet
import math
import bullet as b

def ship_move(x,y,left,right,up,down):
	#Change coordinates as necessary
	#check if outside boundary
	if left and 50 < x: ###ship left boundary
		x-=5
	elif right and x < 550:	###ship right boundary
		x+=5
	if up and y < 750:	###ship upper boundary
		y+=5
	elif down and 200 < y:	###ship lower boundary
		y-=5
	return [x,y]		###just edit them dimensions to your likings

def ship_gun(x,y,modifiers):
	#modifiers = stats
	#create bullet object/class if cooldown = 0
	bullet = b.bullet() #??, make var bullet an object bullet from bullet.py
	bullet.obj_x = x
	bullet.obj_y = y
	bullet.obj_vy = 10
	return bullet

def ship_melee(x,y,modifiers):
	#modifiers=stats
	#create melee class if cooldown = 0
	return attack

def ship_dash(x,y,left,right,up,down,modifiers):
	#modifiers=stats
	#dahses to a certain direction
	return [x,y]

