from time import sleep
import picamera
import picamera.array
import numpy as np
from PIL import Image

if __name__== '__main__':
    camera = picamera.PiCamera()
    camera.color_effects = (128, 128) # The reason why grey image
    # camera.resolution = camera.MAX_RESOLUTION  #To save in PNG format, I have to comment this.
    # Also,if I dont define the resolution, it will be in max resolution, who is 1920,1080
    camera.start_preview(resolution=(410,313),fullscreen=False,window=(20,20,820,616))
    camera.exposure_mode = 'auto'
    
    sleep(2)
    camera.capture('/home/pi/Documents/diffusercam/bernat/from_camera/test14/h_b.png', 'png')



    # for k in range(0,20):
    #     name='/home/pi/Documents/diffusercam/bernat/from_camera/test14/alpha'+str(k)+'.png'
    #     print(k*5,'%')
    #     # sleep(2)
    #     camera.capture(name, 'png')

    camera.stop_preview()

    # for i in range(1):
    #     stream = picamera.array.PiBayerArray(camera)
    #     camera.capture(stream, 'png')
    #     # camera.capture(stream, 'jpeg', bayer=True)
    #     #I added this next 2 lines to get a photo after 3 seconds
    #     # sleep(3)
    #     # camera.capture('/home/pi/Documents/diffusercam/saved_images/test01/t1d0.png')

    #     input("Press Enter to stop")