import picamera
import picamera.array
import numpy as np
from matplotlib import pyplot as plt
from io import BytesIO
from PIL import Image
from imageio import imwrite

def resize_and_fix_origin(kernel, size):
    """Pads a kernel to reach shape size, and shift it in order to cancel phase.
    This is based on the assumption that the kernel is centered in image space.
    """
    pad0, pad1 = size[0]-kernel.shape[0], size[1]-kernel.shape[1]
    # shift less if kernel is even, to start with 2 central items
    shift0, shift1 = (kernel.shape[0]-1)//2, (kernel.shape[1]-1)//2

    kernel = np.pad(kernel, ((0,pad0), (0,pad1)), mode='constant')
    kernel = np.roll(kernel, (-shift0, -shift1), axis=(0,1))
    return kernel

def fast_convolution(image, kernel):

    bfft = np.fft.fft2(image)
    kfft = np.fft.fft2(resize_and_fix_origin(kernel, image.shape))
    result = np.fft.ifft2(kfft*bfft).real
    return result

if __name__== '__main__':
    camera = picamera.PiCamera()
    camera.resolution = camera.MAX_RESOLUTION
    camera.start_preview(resolution=(410,313),fullscreen=False,window=(20,20,820,616))
    camera.exposure_mode = 'auto'

    for i in range(1):
        "using BytesIO"
        stream = BytesIO()
        camera.capture(stream, 'jpeg')
        stream.seek(0)
        image = Image.open(stream)
        arr = np.array(image)
        plt.figure()
        plt.imshow(arr)

        arr_grey = np.sum(arr, axis=2)
        corr = fast_convolution(arr_grey, arr_grey.conj())
        plt.figure()
        plt.imshow(corr, cmap='viridis')
        plt.colorbar()

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

