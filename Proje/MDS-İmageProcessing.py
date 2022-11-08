import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob, os


path = 'org'
resizedlist = dict()

def isle(img):
    im_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #print(im_RGB[0][0])
    im_GRAY = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #x.dtype #kanal bilgisi
    #Görüntü dışarı çıkartma
    #cv2.imwrite("resim.jpg",im_GRAY)
    
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(im_GRAY, (5,5), 0) 
    
    
    #adaptiveThreshold
    thresh1 = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, 127,15)
    
    
    for i in range(0,thresh1.shape[0]):
        for j in range(0,thresh1.shape[1]):
            if thresh1[i][j]==255:
                thresh1[i][j]=0
            elif thresh1[i][j]==0:
                thresh1[i][j]=255
    
    
    #contours, hierarchy = cv2.findContours(thist,bins = np.histogram(img.flatten(),256,[0,256])
    
    
    #im_RGB = cv2.cvtColor(thresh1, cv2.COLOR_GRAY2RGB)
    
    return thresh1
    
klasor="gray"
    
pref="islenen-"+klasor


for infile in glob.glob(os.path.join(path,'*.jpg')):
  imge = cv2.imread(infile)
  islenen=isle(imge)
  isim=infile.split("\\")[1].split(".")[0]
  cv2.imwrite(f"{klasor}/{isim}-{pref}.jpg",islenen)








