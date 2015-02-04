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

#####
# TODO description
#####
def testHelper():
	ledMatrix = [[[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]],
				 [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]],
				 [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]],
				 [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]],
				 [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]],
				 [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]],
				 [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]],
				 [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]]
				]

#####
# TODO description
#####
def getTransformNames():
	return _transformNames

#####
# TODO description
#####
def generateSingleColourMatrix(r, g, b):
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

	# Check paint delay is valid
	if (paintDelay < 0):
		raise ValueError('paintDelay must be 0 or greater')
		return

#####
# TODO description
#####
def applyRandomTransform(ledMatrix, paintDelay):
	# TODO choose a random transform
	applyTransform(ledMatris, "TODO", paintDelay)
