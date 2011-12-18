import pyglet

def center_image(image):
	"""Sets an image's anchor point to its center"""
	image.anchor_x = image.width/2
	image.anchor_y = image.height/2



pyglet.resource.path = ['Content']
pyglet.resource.reindex()


player_image = pyglet.resource.image("tri1.png")

center_image(player_image)