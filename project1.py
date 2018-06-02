import cv2,os
import matplotlib.pyplot as plt
import pylab as pl
from roipoly import roipoly


folder = "trainset"
count = 0

img = cv2.imread(os.path.join(folder,filename))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
count += 1
pl.imshow(img2)

MyROI = roipoly(roicolor='r') 