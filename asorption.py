"""
@author: MSG
"""
import pylab, numpy
from PIL import Image
im = Image.open('s1.jpg') # Can be many different formats.
pix = im.load()
im_width, im_height=im.size
wl_offset=380.0 # wavelength start value for the spectra
wl_range=320.0 # wavelength range for the spectra (380 to 720)
wl_p_pix=wl_range/im_width

x_all=[]
y_all=[]
    
for i in range(0,im_width):      
    x_sum=0.0
    for j in range(0,im.height):      
            x_sum+=sum(pix[i,j])   
            
    x_all.append(i*wl_p_pix+wl_offset)
    y_all.append(x_sum)
    
y_max=max(y_all)
y_all=numpy.array(y_all,dtype='f')
y_trans=y_all/y_max
y_abs=1-y_trans
index_max=numpy.where(y_abs==max(y_abs))
index_max=numpy.array(index_max,dtype='i')
index_max=index_max*wl_p_pix+wl_offset
    
#pylab.plot(x_all, y_trans, c='red', linewidth=2.0)

pylab.plot(x_all, y_abs, c='blue', linewidth=2.0)
pylab.xlabel('Wavelength (nm)', fontsize = 16)
pylab.ylabel('Absorbance', fontsize = 16)
#pylab.savefig('Spectrum.png')
pylab.show()
