import sys
import os
import time
import pyglet, random, math
from pyglet.window import key
import contentContainer
import playerObject
from camera import Camera

import ctypes

###Getting users PC data

user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)


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
			print "\n I'll pretend that you said 50. \n "
		break
			
		
	else:
		os.system("cls")
		print "\n Come on, you have a least 2 friends, right? \n Try again"




print "Initializing Friend Matrix..."

time.sleep(1)


windowList = []

if friendCount > 30:
	windowCount = 30
else:
	windowCount = friendCount

for i in range(0,windowCount):
	rand_width = random.randint(20,screenWidth/2)
	rand_height = random.randint(20, screenHeight/2)

	rand_x = random.randint(0, screenWidth -rand_width )
	rand_y = random.randint(0, screenHeight -rand_height )

	game_window = pyglet.window.Window(rand_width,rand_height)
	game_window.set_location(rand_x, rand_y)


	game_window.clear()
	windowList.append(game_window)
	time.sleep(0.075)


#time.sleep(5)
for i in range (0,5):
	for window in windowList:
		window.clear()
		window.activate()
		window.switch_to()
		time.sleep(0.05)

for window in windowList:
	window.close()
	time.sleep(0.05)



os.system("cls")
print "\n\n\n\n\n"
print "Intro Complete \n\n"
print "You are not alone \n\n\n"
print "Use the arrow keys to search for your friends \n\n"
print "Press and hold SPACE to hold on to a friend \n\n"
print "Beware: friends will hinder your movements when you hold on to them \n\n"

print "Gather all your friend in one place to terminate the simulation"



windowWidth = 300
windowHeight = 200
windowData = playerObject.Player(windowWidth, windowHeight, screenWidth,screenHeight)

new_game_window = pyglet.window.Window(windowWidth,windowHeight)
new_game_window.set_location(int(windowData.player_px), int(windowData.player_py))



new_game_window.push_handlers(windowData.key_handler)

keys = key.KeyStateHandler()
new_game_window.push_handlers(keys)


friendList = []
#print len(friendList)
for i in range (0,friendCount-1):
	tempFriend = playerObject.Player(windowWidth, windowHeight, screenWidth,screenHeight)
	rand_x = random.randint(windowWidth, screenWidth-windowWidth)
	rand_y = random.randint(windowHeight, screenHeight-windowHeight)
	tempFriend.player_px = rand_x
	tempFriend.player_py = rand_y
	friendList.append(tempFriend)
	#print i

#friendList[0] = playerObject.Player(windowWidth, windowHeight, screenWidth,screenHeight)
friendSprite = pyglet.sprite.Sprite(img=contentContainer.friend_green, x=30, y=20)

camera = Camera((0, 0), 100)

@new_game_window.event
def on_draw():
	
	new_game_window.clear()
#	glClear(GL_COLOR_BUFFER_BIT)
	camera.update()
	camera.x = int(windowData.player_px + windowWidth/2 )
	camera.y = int(screenHeight - (windowData.player_py + windowHeight))
	
	camera.focus(windowWidth, windowHeight)
	#print "Camerta pos: ", camera.x, camera.y

	#player_sprite.draw()

	for friend in friendList:
		friendSprite.x = friend.player_px
		friendSprite.y = friend.player_py
		friendSprite.draw()
		#print "Friend pos: ", friendSprite.x, friendSprite.y
	


@new_game_window.event
def update(dt):

	windowData.update(dt)

	new_game_window.set_location(int(windowData.player_px), int(windowData.player_py))

	capture = False

	if keys[key.SPACE]:
		capture = True
	else:
		capture = False
		windowData.speed = 5
	


	if capture == True:
		for friend in friendList:
			#print "Friend pos: ", friendSprite.x, friendSprite.y
			#print "Camerta pos: ", camera.x, camera.y
			if(friend.player_px > windowData.player_px 
			   and friend.player_px <  windowData.player_px + windowWidth ):

			   if( screenHeight -friend.player_py > windowData.player_py 
			   and screenHeight - friend.player_py < windowData.player_py + windowHeight*1.5 ):
			   #	print "heeeeeeelo \n\n\n\n\n\n\n\n\n"
			   	friend.player_px = windowData.player_px + windowWidth /2
			   	friend.player_py = screenHeight - (windowData.player_py + windowHeight )

			   	windowData.speed = windowData.speed * 0.9
			   	
			   	continue


	###check for win:

	win_x = friendList[0].player_px
	win_y = friendList[1].player_py
	winBool  = False
	for friend in friendList:
		if friend.player_px == win_x:
			if friend.player_py ==  win_y:
				winBool = True
			else:
				winBool = False
		else:
			winBool  = False

		continue
	

	if winBool == True:
		os.system("cls")
		print "\n\n\n\n ALL FRIENDS FOUND \n\n\n\n"
		print "SUCCESS"

		new_game_window.close()	
		time.sleep(5)		   



	# for friend in friendList:
	# 	friend.player_vx = -windowData.player_vx
	# 	friend.player_vy = -windowData.player_vy
	# 	friend.update(dt)
	# 	print friend.player_px, friend.player_py
		


if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/240.0)
	#pyglet.clock.schedule(lambda _: None)
	pyglet.app.run()


