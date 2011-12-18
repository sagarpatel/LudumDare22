import sys
import os
import time
import pyglet, random, math
from pyglet.window import key
import contentContainer
import playerObject

import ctypes

###Getting users PC data

user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)

print screenHeight
print screenWidth


player_sprite = pyglet.sprite.Sprite(img=contentContainer.player_image, x=30, y=20)



######



print ("\n\n\n              Hello and welcome to what's supposed to be Alone \n\n\n")



######intro ugly loop

while True:

	print "\n"

	friendCount = int(raw_input("How many freinds do you have?: "))

	print "\n"

	if friendCount > 1 :

		print "Value recieved"
		if friendCount > 50:
			friendCount = 50
		break
			
		
	else:
		os.system("cls")
		print "\n Come on, you have a least 1 friend, right? \n Try again"


	
	



print "Initializing Friend Matrix..."

time.sleep(3)

windowList = []


for i in range(0,friendCount):
	rand_width = random.randint(20,screenWidth/2)
	rand_height = random.randint(20, screenHeight/2)

	rand_x = random.randint(0, screenWidth)
	rand_y = random.randint(0, screenHeight)

	game_window = pyglet.window.Window(rand_width,rand_height)
	game_window.set_location(rand_x, rand_y)


	game_window.clear()
	windowList.append(game_window)
	time.sleep(0.10)


# time.sleep(5)

for window in windowList:
	window.close()
	time.sleep(0.05)


windowWidth = 200
windowHeight = 300
new_game_window = pyglet.window.Window(windowWidth,windowHeight)


windowData = playerObject.Player(windowWidth, windowHeight, screenWidth,screenHeight)
new_game_window.push_handlers(windowData.key_handler)

@game_window.event
def on_draw():
	player_sprite.draw()
	
		





def update(dt):

	windowData.update(dt)

	new_game_window.set_location(int(windowData.player_px), int(windowData.player_py))
	# for window in windowList:
	# 	window.clear()
	# 	window.activate()
	# 	window.switch_to()
	# 	time.sleep(0.1)

		



if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()


