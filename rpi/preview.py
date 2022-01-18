import picamera
import picamera.array
import numpy as np
from matplotlib import pyplot as plt
from io import BytesIO
from PIL import Image
from imageio import imwrite

if __name__== '__main__':
    camera = picamera.PiCamera()
    camera.resolution = camera.MAX_RESOLUTION
    camera.start_preview(resolution=(410,313),fullscreen=False,window=(20,20,820,616))
    camera.exposure_mode = 'auto'
            
    # for i in range(1):
    #     customize = input('Change shutter speed? (y/[n])')
    #     if customize == 'y':
    #         speed = int(input('shutter speed (mus) : '))
    #         camera.shutter_speed = speed 
    #     input('Press enter to take picture ')
    #     stream = picamera.array.PiBayerArray(camera)
    #     camera.capture(stream, 'jpeg', bayer=True)
    #     filename = input('Name of file: ')
    #     arr = np.sum(stream.array,axis=2).astype(np.uint8)
    #     img = Image.fromarray(arr)
    #     img.save(filename)

    for i in range(1):
        "using BytesIO"
        stream = BytesIO()
        camera.capture(stream, 'jpeg')
        stream.seek(0)
        image = Image.open(stream)
        arr = np.array(image)
        plt.figure()
        plt.imshow(arr)

        # image.save("test.jpg")
        
        "using picamera"
        # stream = picamera.array.PiBayerArray(camera)
        # camera.capture('test_pi.jpg')

        # camera.capture(stream, 'jpeg', bayer=True)
        # arr = stream.array
        # print(stream.array.shape)
        # arr = np.sum(stream.array,axis=2).astype(np.uint8)
        # print(arr.shape)

        # print(arr[:5,:5,0])
        # print(arr[:5,:5,1])
        # print(np.max(arr))

        # plt.figure()
        # plt.imshow(arr[:,:,1])
        # plt.show()

        # imwrite('test.jpg', arr)
        # img = Image.fromarray(arr)
        # img.save('test.jpg')
    camera.stop_preview()
    plt.show()

