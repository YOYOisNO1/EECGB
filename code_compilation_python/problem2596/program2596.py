    import numpy as np
    import cv2
    from matplotlib import pyplot as plt
    
    '''
    path = "/home/beatrice/code/codeforce/fourierDoodles/"
    
    i = 1
    for i in range(1,21,1):
        img = cv2.imread(path + str(i) + ".png",0)
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20*np.log(np.abs(fshift))
    
        plt.subplot(121),plt.imshow(img, cmap = 'gray')
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
        plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
        plt.show()
    '''
    
    a = str(input())
    
def bool2Bit(b):
      if(b):
        return '1'
      return '0'
    
def secretFunction(id):
        return (( min ( id , 25 ) + id ) % ( 2 + id % 3 )) > 0
    
    for i in range(21,51,1):
        print(bool2Bit(secretFunction(i)))