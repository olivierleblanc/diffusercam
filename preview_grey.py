import picamera
import picamera.array
import numpy as np
from PIL import Image

if __name__== '__main__':
    camera = picamera.PiCamera()
    camera.color_effects = (128, 128) # The reason why grey image
    camera.resolution = camera.MAX_RESOLUTION
    camera.start_preview(resolution=(410,313),fullscreen=False,window=(20,20,820,616))
    camera.exposure_mode = 'auto'
            
    for i in range(1):
        stream = picamera.array.PiBayerArray(camera)
        camera.capture(stream, 'jpeg', bayer=True)

        input("Press Enter to stop")
