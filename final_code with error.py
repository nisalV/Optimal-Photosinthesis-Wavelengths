#!/usr/bin/env python
# coding: utf-8

# # Take Home Experiment 6
# ## Spectrum Analyzer

# In[156]:


import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# In[157]:


im = Image.open('5.1.jpg')
pix = im.load()
#im.show()
#plt.imshow(im)


# In[158]:


width, height=im.size
#print(height)
#print(width)


# In[159]:


x_all=[]
y_all=[]
wl_start=380
wl_end=750
wl_range=wl_end-wl_start
wl_p_pix=wl_range/width
print(wl_p_pix)


# In[160]:


for i in range(0,width):      
    s = 0.0
    c = 0
    for j in range(0,height):
        RGB=pix[i,j]
        #s+=sum(RGB)/3                                            #avarage method
        s+=0.21*int(RGB[0]) + 0.72*int(RGB[1]) + 0.07*int(RGB[2]) #luminosity method
        c += 1.0   
            
    x_all.append(i*wl_p_pix+wl_start)
    y_all.append(s/c)

y_all=np.array(y_all)   
y_all=y_all/max(y_all)

y_all=y_all[::-1]


# In[161]:


index_max=np.where(y_all==max(y_all))
index_max=np.array(index_max,dtype='i')
peak_start=(index_max[0][0]-1)*wl_p_pix+wl_start
last_index=len(index_max)
peak_end=(index_max[last_index-1][0])*wl_p_pix+wl_start
max_x=(peak_end+peak_start)/2
print('peak starting wavelength: '+str(peak_end)+'nm')
print('peak starting wavelength: '+str(peak_start)+'nm')
print('max intensity wavelength: '+str(max_x)+' nm')
max_in_wl_err=(peak_end-peak_start)/2
print('error of maximum intensity wavelength: '+str(max_in_wl_err)+'nm')


# In[162]:


plt.plot(x_all,y_all, c='blue', linewidth=2.0,label='the graph')
plt.xlabel('wavelength (nm)', fontsize = 16)
plt.ylabel('intensity', fontsize = 16)
plt.title('The graph of intensity vs Wavelengh', fontsize = 16)
plt.vlines(x=max_x, ymin=0, ymax= max(y_all), ls='--',color='red',label='x=%.1f'%(max_x))
plt.hlines(y=max(y_all), xmax=max_x,xmin=min(x_all), ls='--',color='green',label='y=1')
plt.legend()
plt.annotate('maximum intensity (x=%.1f,y=1)'%(max_x), xy=(max_x, max(y_all)), xytext=(600, max(y_all)),
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))

plt.show()


# In[163]:

"""
max_in_color=''
if max_x<450:
    max_in_color='violat'
elif max_x<495:
    max_in_color='blue'
elif max_x<570:
    max_in_color='green'
elif max_x<590:
    max_in_color='yellow'   
elif max_x<620:
    max_in_color='orange' 
else:
    max_in_color='red'  
    
print('max intensity colour: '+max_in_color)    


# In[164]:


lamda=float(max_x)*(pow(10,-9))
T=(2.898*(pow(10,-3)))/lamda
print('temparature on sun '+str(T)+ ' K')
"""

# In[ ]:




