from time import sleep
import picamera
import picamera.array
import numpy as np
from PIL import Image

if __name__== '__main__':
    camera = picamera.PiCamera()
    camera.color_effects = (128, 128) # The reason why grey image
    camera.resolution = camera.MAX_RESOLUTION
    camera.start_preview(resolution=(410,313),fullscreen=True)#,window=(20,20,820,616))
    camera.exposure_mode = 'auto'
            
    for i in range(1):
        stream = picamera.array.PiBayerArray(camera)
        camera.capture(stream, 'jpeg', bayer=True)
        #I added this next 2 lines to get a photo after 3 seconds
        # sleep(3)
        # camera.capture('/home/pi/Documents/diffusercam/saved_images/test01/t1d0.jpg')

        input("Press Enter to stop")

