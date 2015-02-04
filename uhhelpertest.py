import unicornhathelper as ledHelper
import time

myMatrix = [ [ [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255] ],
             [ [0, 0, 255], [255, 0, 0], [255, 0, 0], [0, 0, 255], [0, 0, 255], [255, 0, 0], [255, 0, 0], [0, 0, 255] ],
             [ [255, 0, 0], [0, 255, 0], [0, 255, 0], [255, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 0], [255, 0, 0] ],
             [ [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [255, 0, 0] ],
             [ [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [255, 0, 0] ],
             [ [0, 0, 255], [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [255, 0, 0], [0, 0, 255] ],
             [ [0, 0, 255], [0, 0, 255], [255, 0, 0], [0, 255, 0], [0, 255, 0], [255, 0, 0], [0, 0, 255], [0, 0, 255] ],
             [ [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 0, 0], [255, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255] ]
           ]

ledHelper.applyTransform(myMatrix, "test1", 0.2)
time.sleep(3)
ledHelper.clearLEDs()
ledHelper.applyTransform(myMatrix, "test2", 0.2)
time.sleep(3)
ledHelper.clearLEDs()
ledHelper.applyTransform(myMatrix, "test3", 0.2)
time.sleep(3)
ledHelper.clearLEDs()
ledHelper.applyTransform(myMatrix, "test4", 0.2)
time.sleep(3)
ledHelper.clearLEDs()
ledHelper.applyTransform(myMatrix, "test5", 0.2)
time.sleep(3)
ledHelper.clearLEDs()
ledHelper.applyTransform(myMatrix, "test6", 0.2)

while True:
	time.sleep(1)
