import sys
import os
import time
import pyglet, random, math
import contentContainer


print ("\n\n\n              Hello and welcome to what's supposed to be Alone \n\n\n")





######intro ugly loop

while True:

	print "\n"

	userHeight = int(raw_input("How tall are you (in cm)?: "))

	print "\n"

	if userHeight > 50 :

		if userHeight < 250:
			print "Valid height"
			break

		else:
			os.system("cls")
			print "\n A little too tall, don't you think? \n Try again"
			
		
	else:
		os.system("cls")
		print "\n Sorry, you need to be above the minimum height requirement \n Try again"


	
	




print "Broken out!"

print "Now creating window..."

time.sleep(3)






