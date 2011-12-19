import math
from pyglet.window import key
import pyglet


class Player():
	def __init__(self, windowW, windowH, screenW, screenH):
		self.key_handler = key.KeyStateHandler()

		self.player_vx = 0
		self.player_vy = 0
		self.player_px = 200
		self.player_py = 300

		self.windowWidth = windowW
		self.windowHeight = windowH

		self.screenWidth = screenW
		self.screenHeight = screenH

		self.speed = 5
		self.friction = 0.99

	
	
	def update(self, dt):
	
		if self.key_handler[key.LEFT]:
			self.player_vx -= 1 * self.speed
		if self.key_handler[key.RIGHT]:
			self.player_vx += 1 * self.speed
		if self.key_handler[key.UP]:
			self.player_vy -= 1 * self.speed
		if self.key_handler[key.DOWN]:
			self.player_vy += 1 * self.speed

		if self.windowWidth + self.player_px > self.screenWidth:
			self.player_vx = -self.player_vx
		if self.player_px < 0:
			self.player_vx = -self.player_vx
		if self.windowHeight + self.player_py > self.screenHeight:
		 	self.player_vy = -self.player_vy
		if self.player_py < 0:
		 	self.player_vy = -self.player_vy
		 	
		 
		self.player_vx = self.player_vx * self.friction
		self.player_vy = self.player_vy * self.friction

		if abs(self.player_vx) < 2 :
			self.player_vx = 0
		if abs(self.player_vy) < 2 :
			self.player_vy = 0 
		
		self.player_px += self.player_vx * dt
		self.player_py += self.player_vy * dt

