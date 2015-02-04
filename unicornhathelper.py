#####
# 
# Name:    unicornhathelper.py
#
# Purpose: TODO
#
# Author:  Simon Prickett
#
#####

import unicornhat as UH
import time

#####
# TODO descriptions
#####
_transformNames = [ 
	'leftToRightBlind', 
	'rightToLeftBlind', 
	'topToBottomBlind', 
	'bottomToTopBlind', 
	'verticalBlindsEdgesToCenter',
	'verticalBlindsCenterToEdges',
	'horiztontalBlindsEdgesToCenter', 
	'horizontalBlindsCenterToEdges',
	'pour', 
	'horizontalLineByLineTopDown', 
	'horizontalLineByLineBottomUp', 
	'verticalLineByLineTopDown', 
	'verticalLineByLineBottomUp',
	'horizontalSnakeFromTop', 
	'verticalSnakeFromTop', 
	'snakeFromCenter', 
	'radiateFromBottomLeft', 
	'radiateFromTopLeft',
	'random', 
	'opposingHorizontals', 
	'opposingVerticals'
]

# What a simple transform looks like...
# Remember a step may involve >1 LED...
# top to bottom line by line
_testTransform = [
	[ [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1] ],
	[ [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2] ],
	[ [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3] ],
	[ [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4] ],
	[ [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5] ],
	[ [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [8, 6] ],
	[ [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7] ],
	[ [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8] ]
]

#top to bottom half a line at a time
_testTransform2 = [
	[ [1, 1], [2, 1], [3, 1], [4, 1] ], 
	[ [5, 1], [6, 1], [7, 1], [8, 1] ],
	[ [1, 2], [2, 2], [3, 2], [4, 2] ],
	[ [5, 2], [6, 2], [7, 2], [8, 2] ],
	[ [1, 3], [2, 3], [3, 3], [4, 3] ], 
	[ [5, 3], [6, 3], [7, 3], [8, 3] ],
	[ [1, 4], [2, 4], [3, 4], [4, 4] ],
	[ [5, 4], [6, 4], [7, 4], [8, 4] ],
	[ [1, 5], [2, 5], [3, 5], [4, 5] ], 
	[ [5, 5], [6, 5], [7, 5], [8, 5] ],
	[ [1, 6], [2, 6], [3, 6], [4, 6] ], 
	[ [5, 6], [6, 6], [7, 6], [8, 6] ],
	[ [1, 7], [2, 7], [3, 7], [4, 7] ], 
	[ [5, 7], [6, 7], [7, 7], [8, 7] ],
	[ [1, 8], [2, 8], [3, 8], [4, 8] ], 
	[ [5, 8], [6, 8], [7, 8], [8, 8] ]
]

# vertical blinds sides to center
_testTransform3 = [
	[ [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8] ],
	[ [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8] ],
	[ [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8] ],
	[ [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8] ]
]

# TODO
_testTransform4 = [
	[ [4, 4], [5, 4], [4, 5], [5, 5] ],
	[ [6, 4], [7, 4], [6, 5], [7, 5] ],
	[ [6, 2], [7, 2], [6, 3], [7, 3] ],
	[ [4, 2], [5, 2], [4, 3], [5, 3] ],
	[ [2, 2], [3, 2], [2, 3], [3, 3] ],
	[ [2, 4], [3, 4], [2, 5], [3, 5] ],
	[ [2, 6], [3, 6], [2, 7], [3, 7] ],
	[ [4, 6], [5, 6], [4, 7], [5, 7] ],
	[ [6, 6], [6, 7], [7, 6], [7, 7] ],
	[ [8, 6], [8, 7] ],
	[ [8, 4], [8, 5] ],
	[ [8, 2], [8, 3] ],
	[ [8, 1], [7, 1] ],
	[ [6, 1], [5, 1] ],
	[ [4, 1], [3, 1] ],
	[ [2, 1], [1, 1] ],
	[ [1, 2], [1, 3] ],
	[ [1, 4], [1, 5] ],
	[ [1, 6], [1, 7] ],
	[ [1, 8], [2, 8] ],
	[ [3, 8], [4, 8] ],
	[ [5, 8], [6, 8] ],
	[ [7, 8], [8, 8] ]
]

#####
# TODO description
#####
def getTransformNames():
	return _transformNames

#####
# TODO description
#####
def generateSingleColorMatrix(r, g, b):
	if (r < 0 or r > 255):
		raise ValueError('r must be between 0 and 255')
		return
	if (g < 0 or r > 255):
		raise ValueError('g must be between 0 and 255')
		return
	if (b < 0 or r > 255):
		raise ValueError('b must be between 0 and 255')
		return

	singleRow = [[r, g, b], [r, g, b], [r, g, b], [r, g, b], [r, g, b], [r, g, b], [r, g, b], [r, g, b]]

	return [singleRow, singleRow, singleRow, singleRow, singleRow, singleRow, singleRow, singleRow]

#####
# TODO description
#####
def applyTransform(ledMatrix, tranformName, paintDelay):
	# Check ledMatrix is valid
	#TODO

	# Check transformName is valid
	#TODO
	transformMatrix = _testTransform4

	# Check paint delay is valid
	if (paintDelay < 0):
		raise ValueError('paintDelay must be 0 or greater')
		return

	print ledMatrix
	for nextStepLEDs in transformMatrix:
		print nextStepLEDs
		for individualLED in nextStepLEDs:
			x = individualLED[0] - 1
			y = individualLED[1] - 1
			print "x = " + str(x) + ", y = " + str(y)
			
			colorsToPaint = ledMatrix[x][y]
			r = colorsToPaint[0]
			g = colorsToPaint[1]
			b = colorsToPaint[2]
			UH.set_pixel(x, y, r, g, b)
			print "set to r = " + str(r) + ", g = " + str(g) + ", b = " + str(b)

		UH.show()
		time.sleep(paintDelay)

#####
# TODO description
#####
def applyRandomTransform(ledMatrix, paintDelay):
	# TODO choose a random transform
	applyTransform(ledMatrix, "TODO", paintDelay)
