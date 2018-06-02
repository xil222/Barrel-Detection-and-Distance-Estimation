
# coding: utf-8

# In[1]:

import cv2,os
import matplotlib.pyplot as plt
import pylab as pl
import scipy.io as sio 
import numpy as np
import scipy.stats
import math
from skimage import measure
from skimage import data, util
from skimage.measure import label, regionprops




# In[2]:

folder = "trainset"

YchannelR = []
CrchannelR = []
CbchannelR = []

YchannelnR = []
CrchannelnR = []
CbchannelnR = []

YchannelY = []
CrchannelY = []
CbchannelY = []

YchannelBr = []
CrchannelBr = []
CbchannelBr = []


# In[3]:

img = cv2.imread(os.path.join(folder,'2.2.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label2.2.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])


# In[4]:

#classes for non-red barrel
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])

#classes for yellow
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])

#classes for brown
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])


# In[5]:

cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[6]:

img = cv2.imread(os.path.join(folder,'2.3.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label2.3.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[7]:

img = cv2.imread(os.path.join(folder,'2.8.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label2.8.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[8]:

img = cv2.imread(os.path.join(folder,'2.14.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label2.14.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[9]:

img = cv2.imread(os.path.join(folder,'2_3.1.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label2_3.1.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[10]:

img = cv2.imread(os.path.join(folder,'3.1.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label3.1.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[11]:

img = cv2.imread(os.path.join(folder,'3.2.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label3.2.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[12]:

img = cv2.imread(os.path.join(folder,'3.4.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label3.4.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[13]:

img = cv2.imread(os.path.join(folder,'3.10.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label3.10.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[14]:

img = cv2.imread(os.path.join(folder,'4.1.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label4.1.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[15]:

img = cv2.imread(os.path.join(folder,'4.3.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label4.3.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[16]:

img = cv2.imread(os.path.join(folder,'4.5.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label4.5.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[17]:

img = cv2.imread(os.path.join(folder,'4.7.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label4.7.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[18]:

img = cv2.imread(os.path.join(folder,'4.10.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label4.10.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[19]:

img = cv2.imread(os.path.join(folder,'5.1.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label5.1.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[20]:

img = cv2.imread(os.path.join(folder,'5.2.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label5.2.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[21]:

img = cv2.imread(os.path.join(folder,'5.9.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label5.9.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[22]:

img = cv2.imread(os.path.join(folder,'5.11.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label5.11.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[23]:

img = cv2.imread(os.path.join(folder,'6.5.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label6.5.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[24]:

img = cv2.imread(os.path.join(folder,'7.2.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label7.2.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[25]:

img = cv2.imread(os.path.join(folder,'7.3.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label7.3.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[26]:

img = cv2.imread(os.path.join(folder,'8.2.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label8.2.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[27]:

img = cv2.imread(os.path.join(folder,'8.4.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label8.4.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[28]:

img = cv2.imread(os.path.join(folder,'9.2.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label9.2.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[29]:

img = cv2.imread(os.path.join(folder,'10.4.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label10.4.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[30]:

img = cv2.imread(os.path.join(folder,'14.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label14.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[31]:

img = cv2.imread(os.path.join(folder,'2.6.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label2.6.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[32]:

img = cv2.imread(os.path.join(folder,'3.8.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label3.8.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[33]:

img = cv2.imread(os.path.join(folder,'3.11.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label3.11.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[34]:

img = cv2.imread(os.path.join(folder,'4.2.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label4.2.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[35]:

img = cv2.imread(os.path.join(folder,'4.4.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label4.4.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[36]:

img = cv2.imread(os.path.join(folder,'4.6.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label4.6.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[37]:

img = cv2.imread(os.path.join(folder,'4.8.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label4.8.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[38]:

img = cv2.imread(os.path.join(folder,'5.3.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label5.3.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[39]:

img = cv2.imread(os.path.join(folder,'5.4.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label5.4.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[40]:

img = cv2.imread(os.path.join(folder,'5.5.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label5.5.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[41]:

img = cv2.imread(os.path.join(folder,'5.6.png'))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
data = sio.loadmat('label5.6.mat')
xR = data['xR'].reshape([-1,1])
yR = data['yR'].reshape([-1,1])
xnR = data['xnR'].reshape([-1,1])
ynR = data['ynR'].reshape([-1,1])
xY = data['xY'].reshape([-1,1])
yY = data['yY'].reshape([-1,1])
xBr = data['xBr'].reshape([-1,1])
yBr = data['yBr'].reshape([-1,1])
cnt = 0
while cnt< len(xR):
    YchannelR.append(img2[xR[cnt],yR[cnt],0])
    CrchannelR.append(img2[xR[cnt],yR[cnt],1])
    CbchannelR.append(img2[xR[cnt],yR[cnt],2])
    cnt = cnt+1

cnt = 0
while cnt< len(xnR):
    YchannelnR.append(img2[xnR[cnt],ynR[cnt],0])
    CrchannelnR.append(img2[xnR[cnt],ynR[cnt],1])
    CbchannelnR.append(img2[xnR[cnt],ynR[cnt],2])
    cnt = cnt+1
 
cnt = 0
while cnt< len(xY):
    YchannelY.append(img2[xY[cnt],yY[cnt],0])
    CrchannelY.append(img2[xY[cnt],yY[cnt],1])
    CbchannelY.append(img2[xY[cnt],yY[cnt],2])
    cnt = cnt+1 

cnt = 0
while cnt< len(xBr):
    YchannelBr.append(img2[xBr[cnt],yBr[cnt],0])
    CrchannelBr.append(img2[xBr[cnt],yBr[cnt],1])
    CbchannelBr.append(img2[xBr[cnt],yBr[cnt],2])
    cnt = cnt+1


# In[95]:

#append the width and height of all barrels above
width=[183,191,208,245,173,146,119,143,115,103,100,90,98,95,80,80,82,78,64,62,66,47,48,35,40,29,243,137,135,106,95,106,115,80,89,79,79]
height=[234,238,305,326,215,187,167,197,162,151,131,134,131,137,118,118,111,116,91,76,84,74,77,61,56,40,330,208,197,158,130,156,160,115,120,110,111]
bias = (np.ones((len(width),1)))

distance = [2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,6,7,7,8,8,9,10,14,2,3,3,4,4,4,4,5,5,5,5]
#is using closed quadratic form the best
#for optimal calculate distance
V = np.identity(len(width))
X = np.hstack((np.reshape(width,(len(width),1)),np.reshape(height,(len(width),1)),bias))
Y = np.reshape(distance,(len(width),1))
w = np.dot(np.dot(np.dot(np.linalg.inv(np.dot(np.dot(np.transpose(X),np.linalg.inv(V)),X)),np.transpose(X)),np.linalg.inv(V)),Y)


# In[44]:

covchannelR = np.zeros((3,3))
meanYchannelR = np.sum(YchannelR)/len(YchannelR)
meanCrchannelR = np.sum(CrchannelR)/len(CrchannelR)
meanCbchannelR = np.sum(CbchannelR)/len(CbchannelR)
meanR = np.reshape([meanYchannelR,meanCrchannelR,meanCbchannelR],(3,1))
channelR = np.hstack((YchannelR,CrchannelR,CbchannelR))
i = 0
while i < len(YchannelR):
    covchannelR = covchannelR + np.dot((np.reshape(channelR[i,:],(3,1))-meanR),np.transpose(np.reshape(channelR[i,:],(3,1))-meanR))
    i += 1
avgcovchannelR = covchannelR/len(YchannelR)

covchannelnR = np.zeros((3,3))
meanYchannelnR = np.sum(YchannelnR)/len(YchannelnR)
meanCrchannelnR = np.sum(CrchannelnR)/len(CrchannelnR)
meanCbchannelnR = np.sum(CbchannelnR)/len(CbchannelnR)
meannR = np.reshape([meanYchannelnR,meanCrchannelnR,meanCbchannelnR],(3,1))
channelnR = np.hstack((YchannelnR,CrchannelnR,CbchannelnR))
i = 0
while i < len(YchannelnR):
    covchannelnR = covchannelnR + np.dot((np.reshape(channelnR[i,:],(3,1))-meannR),np.transpose(np.reshape(channelnR[i,:],(3,1))-meannR))
    i += 1
avgcovchannelnR = covchannelnR/len(YchannelnR)

covchannelY = np.zeros((3,3))
meanYchannelY = np.sum(YchannelY)/len(YchannelY)
meanCrchannelY = np.sum(CrchannelY)/len(CrchannelY)
meanCbchannelY = np.sum(CbchannelY)/len(CbchannelY)
meanY = np.reshape([meanYchannelY,meanCrchannelY,meanCbchannelY],(3,1))
channelY = np.hstack((YchannelY,CrchannelY,CbchannelY))
i = 0
while i < len(YchannelY):
    covchannelY = covchannelY + np.dot((np.reshape(channelY[i,:],(3,1))-meanY),np.transpose(np.reshape(channelY[i,:],(3,1))-meanY))
    i += 1
avgcovchannelY = covchannelY/len(YchannelY)

covchannelBr = np.zeros((3,3))
meanYchannelBr = np.sum(YchannelBr)/len(YchannelBr)
meanCrchannelBr = np.sum(CrchannelBr)/len(CrchannelBr)
meanCbchannelBr = np.sum(CbchannelBr)/len(CbchannelBr)
meanBr = np.reshape([meanYchannelBr,meanCrchannelBr,meanCbchannelBr],(3,1))
channelBr = np.hstack((YchannelBr,CrchannelBr,CbchannelBr))
i = 0
while i < len(YchannelBr):
    covchannelBr = covchannelBr + np.dot((np.reshape(channelBr[i,:],(3,1))-meanBr),np.transpose(np.reshape(channelBr[i,:],(3,1))-meanBr))
    i += 1
avgcovchannelBr = covchannelBr/len(YchannelBr)


# In[45]:

detR = np.linalg.det(avgcovchannelR)
detnR = np.linalg.det(avgcovchannelnR)
detY = np.linalg.det(avgcovchannelY)
detBr = np.linalg.det(avgcovchannelBr)


# In[46]:

#pixel is 1*3
def findcolorclass(image):
    colormatrix = np.zeros((image.shape[0],image.shape[1]),dtype = np.uint8)
    binarymatrix = np.zeros((image.shape[0],image.shape[1]), dtype = np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            probR = 1/np.sqrt(np.power(2*math.pi,3)*detR)*np.exp((-1/2)*np.dot(np.dot(np.transpose(np.reshape(image[i][j],(3,1))-meanR),np.linalg.inv(avgcovchannelR)),np.reshape(image[i][j],(3,1))-meanR))
            probnR = 1/np.sqrt(np.power(2*math.pi,3)*detnR)*np.exp((-1/2)*np.dot(np.dot(np.transpose(np.reshape(image[i][j],(3,1))-meannR),np.linalg.inv(avgcovchannelnR)),np.reshape(image[i][j],(3,1))-meannR))
            probY = 1/np.sqrt(np.power(2*math.pi,3)*detY)*np.exp((-1/2)*np.dot(np.dot(np.transpose(np.reshape(image[i][j],(3,1))-meanY),np.linalg.inv(avgcovchannelY)),np.reshape(image[i][j],(3,1))-meanY))
            probBr = 1/np.sqrt(np.power(2*math.pi,3)*detBr)*np.exp((-1/2)*np.dot(np.dot(np.transpose(np.reshape(image[i][j],(3,1))-meanBr),np.linalg.inv(avgcovchannelBr)),np.reshape(image[i][j],(3,1))-meanBr))
            proball = [probR,probnR,probY,probBr]
            colormatrix[i][j] = proball.index(max(proball))
            if proball.index(max(proball)) == 0:
                binarymatrix[i][j] = 1
            else:
                binarymatrix[i][j] = 0
    return colormatrix,binarymatrix


# In[97]:

folder = "testset"
noimg = 1
for filename in os.listdir(folder):
    newimg = cv2.imread(os.path.join(folder,filename))
    newimg = scipy.misc.imresize(newimg,[900,1200,3],'nearest')
    newimg2 = cv2.cvtColor(newimg, cv2.COLOR_BGR2YCR_CB)
    colormap,binarymap = findcolorclass(newimg2)
    (_,contours,_) =cv2.findContours(binarymap,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    binarymatrix = np.zeros((newimg.shape[0],newimg.shape[1]), dtype = np.uint8)
    plt.imshow(colormap)
    plt.show()
    
    arrayc = np.array(contours)
    deletecontour = []
    bigarea = []
    i = 0
    numcontour = 0
    while i < len(arrayc):
        area = cv2.contourArea(arrayc[i])
        if area<1000:
            deletecontour.append(i)
        else:
            print(area)
            bigarea.append(area)
        i += 1
    newarray = np.delete(arrayc, deletecontour, axis=0)
    newcontour = list(newarray)

    boxc = 0
    boxp = []
    while boxc < newarray.shape[0]:
        rotrect = cv2.minAreaRect(newarray[boxc])
        box = cv2.boxPoints(rotrect)
        box = np.int0(box)
#cv2.drawContours(binarymatrix, [box], -1, 255, 2)
#cv2.imshow('image', binarymatrix); cv2.waitKey(0)
        boxh = np.sqrt(np.square(box[0][0]-box[3][0])+np.square(box[0][1]-box[3][1]))
        boxw = np.sqrt(np.square(box[0][0]-box[1][0])+np.square(box[0][1]-box[1][1]))
        boxarea = boxh * boxw
        print(boxarea)
        print(float(bigarea[boxc]/boxarea))
        barrelness = float(bigarea[boxc]/boxarea)
        boxc += 1
        if barrelness > 0.75:
            boxp.append(box)
    abbox = np.array(boxp)
    numb = abbox.shape[0]
    if numb == 0:
        print("ImageNo =" ,noimg, "no barrels detected")
    
    elif numb == 1:
        BLX = min(box[2][0],box[0][0])
        BLY = max(box[2][1],box[0][1])
        TRX = max(box[2][0],box[0][0])
        TRY = min(box[2][1],box[0][1])
        mdistance = np.dot(np.reshape([boxw,boxh],(1,2)),[w[0],w[1]])+w[2]
        print("ImageNo =" ,noimg, "BottomLeftX =" ,BLX, "BottomLeftY =", BLY,
    "TopRightX =", TRX, "TopRightY =", TRY, "Distance =", mdistance,'\n')
    else:
        abbox = np.reshape(abbox,(abbox.shape[0]*abbox.shape[1],abbox.shape[2]))
        TRX = max(abbox[:,0]) 
        BLX = min(abbox[:,0])
        BLY = max(abbox[:,1])
        TRY = min(abbox[:,1])
        boxh = TRX-BLX
        boxw = BLY-TRY
        mdistance = np.dot(np.reshape([boxw,boxh],(1,2)),[w[0],w[1]])+w[2]
        print("ImageNo =" ,noimg, "BottomLeftX =" ,BLX, "BottomLeftY =", BLY,
    "TopRightX =", TRX, "TopRightY =", TRY, "Distance =", mdistance,'\n')
    noimg += 1
    if noimg > 10:
        break

#cv2.drawContours(binarymatrix,newcontour,-1,255,1)
#newbinary = cv2.fillPoly(binarymatrix, newcontour, 255)
#cv2.imshow("window title", binarymatrix)
#cv2.waitKey(0)



